from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style = {'input_type':'password'},write_only=True)
    class Meta:
        model = User
        fields = ["email","username","password","password2","tc"]
        extra_kwargs = {
            'password':{'write_only':True}
        }

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError("Password Doesn't Match! ")
        return attrs
    

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    




class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = User
        fields = ["email","password"]




class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","email","username","first_name","last_name"]




class PasswordChangeSerializer(serializers.Serializer):
    password = serializers.CharField(max_length = 255, style= {'input_type':'password'},write_only=True)
    password2 = serializers.CharField(max_length = 255, style= {'input_type':'password'},write_only=True)
    class Meta:
        fields = ["password", "password2"]

    def validate(self, attrs):
        password = attrs.get("password")
        password2 = attrs.get("password2")
        user = self.context.get("user")
        if password != password2:
            raise serializers.ValidationError("Password Doesn't matched")
        user.set_password(password)
        user.save()        
        return attrs