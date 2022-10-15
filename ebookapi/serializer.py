from rest_framework import serializers
from django.contrib.auth.models import User
from ebookapi.models import Books,Review


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Books
        fields="__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=[
            "first_name",
            "last_name",
            "username",
            "password",
            "email"
        ]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class ReviewSerializer(serializers.ModelSerializer):
    book=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    class Meta:
        model=Review
        fields="__all__"
    def create(self, validated_data):
        user=self.context.get("user")
        book=self.context.get("book")
        return Review.objects.create(user=user,book=book,**validated_data)
