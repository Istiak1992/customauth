from rest_framework.authentication import BaseAuthentication
#from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import get_user_model


class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        User = get_user_model()
        role = request.GET.get('role')
        if role is None:
            return None
        elif role == "basic":
            try:
                user = User.objects.get(role=role)
            except User.DoesNotExist:
                raise AuthenticationFailed('User Does Not Exist.')
        
        return (user,None)