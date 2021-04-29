import jwt
from django.conf import settings
from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions
from users.models import User
class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        try:
            head, token = request.META.get("HTTP_AUTHORIZATION").split(" ")
            decoded = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            pk = decoded.get('id')
            user = User.objects.get(pk=pk)
            return (user, None)
        except ValueError:
            return None
        except jwt.exceptions.DecodeError:
            raise exceptions.AuthenticationFailed(detail='jwt format invalid')
