from rest_framework.serializers import ModelSerializer
from .models import User


class MyInfoSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class FeedUserSerializer(ModelSerializer):
    class Meta:
        model = User  # Feed라는 모델이라는 직렬화 할 것이다.
        fields = ("username", "email") # Feed의 모든 field를 직렬화 할 것이다. 
