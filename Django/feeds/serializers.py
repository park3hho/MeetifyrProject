from rest_framework.serializers import ModelSerializer
from .models import Feed
from users.serializers import FeedUserSerializer
from reviews.serializers import ReviewsSerializer

class FeedSerializer(ModelSerializer):

    user = FeedUserSerializer(read_only=True)  # Feed 모델 내에 user라는 필드가 있음
    review_set = ReviewsSerializer(many=True, read_only=True)

    class Meta:
        model = Feed # Feed라는 모델이라는 직렬화 할 것이다.
        fields = "__all__" # Feed의 모든 field를 직렬화 할 것이다. 