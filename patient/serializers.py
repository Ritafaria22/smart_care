from rest_framework import serializers
from . import models
from django.contrib.auth.models import User

class PatientSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model = models.Patient
        fields = '__all__'

class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required = True)
    class Meta:
        model = models.User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password']
        
    def save(self):
        username =  self.validated_data['username']
        first_name =  self.validated_data['first_name']
        last_name =  self.validated_data['last_name']
        email =  self.validated_data['email']
        password =  self.validated_data['password']
        password2 =  self.validated_data['confirm_password']
         
        if password != password2:
            raise serializers.ValidationError({'error': 'Password doesnt match'})
        
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error': 'Email already exist'})
        
        account = User(username=username, email=email, first_name=first_name, last_name=last_name)#jodi uporer shb thik thak hoy tahole account toiri hobe
        print(account)
        account.set_password(password)#account a password set korlam
        account.is_active = False
        account.save()
        return account


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)



