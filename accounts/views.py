from dj_rest_auth.registration.views import RegisterView

from api.serializers.accounts import CustomRegisterSerializer
from rest_framework import status
from rest_framework.response import Response

class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer
    
    def create(self, request, *args, **kwargs):
        mutable_data = request.data.copy()
        mutable_data['username'] = mutable_data['email']
        serializer = self.get_serializer(data=mutable_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        serializer_data = serializer.data
        serializer_data.pop('username')
        headers = self.get_success_headers(serializer.data)
        response_data = {
            "message": "User registered successfully!",
            "data": serializer_data
        }
        return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)