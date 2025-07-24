from rest_framework.serializers import ModelSerializer
from .models import Review
from users.serializers import FeedUserSerializer


class ReviewsSerializer(ModelSerializer):
    
    user = FeedUserSerializer(read_only=True)# Reivew.model 내에 user라는 필드가 이씀 ㅎㅎ 

    class Meta:
        model = Review
        fields = "__all__" 
