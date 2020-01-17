from rest_framework import serializers

class Login_Serializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class Register_Serialzer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    email = serializers.EmailField()