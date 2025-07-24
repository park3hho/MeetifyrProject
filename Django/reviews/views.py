from rest_framework.views import APIView
from .models import Review
from .serializers import ReviewsSerializer
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

# Create your views here.
class Reviews(APIView):
    def get(self, request):
        reviews = Review.objects.all()
        serializer = ReviewsSerializer(reviews, many=True)
        return Response(serializer.data)

class ReviewDetail(APIView):
    def get(self, request, review_id):
        try: 
            review = Review.objects.get(id=review_id)
        except:
            raise NotFound
        
        serializer = ReviewsSerializer(review)
        return Response(serializer.data) 