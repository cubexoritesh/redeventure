from django.contrib.auth import authenticate
from .models import User

from rest_framework.response import Response
from rest_framework.views import APIView

from .AuthSerializers import Login_Serializer
from .AuthSerializers import Register_Serialzer


class Login(APIView):
    def post(self, request):
        serializer = Login_Serializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(username=serializer.data['username'], password=serializer.data['password'])
            if user:
                return Response(status=202, data={'status': 'logged in', 'key': user.get_token()})
            else:
                return Response(status=401, data={'error': 'Invalid Username and password'})
        else:
            return Response(serializer.error_messages)

class Login_user(APIView):
    def get(self, request):
        v1_data = User.objects.filter(username='username', password='password')
        v2_data = Login_Serializer(v1_data, many=True)
        return JsonResponse(v2_data.data)

class Register(APIView):
    def post(self, request):
        serializer = Register_Serialzer(data=request.data)
        if serializer.is_valid():
            register_user = User.objects.create(username=serializer.data['username'], password=serializer.data['password'],
                                email=serializer.data['email'])
            if register_user():
                return Response(status=200, data={'status': 'Registration Success', 'key': user.get_token()})
            else:
                return Response(status=400, data={'error': 'User Already Registered'})
        else:
            return Response(serializer.error_messages)






