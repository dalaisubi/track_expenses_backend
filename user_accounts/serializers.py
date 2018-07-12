from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Profile

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=Profile.objects.all())]
            )
    username = serializers.CharField(
            validators=[UniqueValidator(queryset=Profile.objects.all())]
            )
    password = serializers.CharField(min_length=8)

    def create(self, validated_data):
        user = Profile.objects.create_user(validated_data['username'], validated_data['email'],
             validated_data['password'])
        return user

    class Meta:
        model = Profile
        fields = ('id', 'username', 'email', 'password')