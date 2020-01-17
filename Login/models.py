from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token


class User(AbstractUser):
    pass

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def get_token(self):
        token, created = Token.objects.get_or_create(user=self)
        return token.key
