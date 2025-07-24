from rest_framework.views import APIView # 클래시 기반 뷰 만들기 위해 쓰는 놈
from .models import Feed
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .serializers import FeedSerializer # Serializer에서 가져오기
# Create your views here.
class Feeds(APIView):
    # 전체 게시글 조회
    def get(self,request):
        feeds = Feed.objects.all();
        # 객체 -> JSON (Serialize)
        serialized = FeedSerializer(feeds, many=True)
        return Response(serialized.data)
    
    def post(self, request):
        serializer = FeedSerializer(data=request.data) 
        if serializer.is_valid():       
            feed = serializer.save(user=request.user) # 받은 데이터 저장 시, 유저 데이터도 받아야 함으로 넘겨줘야 함.
            serializer = FeedSerializer(feed)
            print("post serializer", serializer)

            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class FeedDetail(APIView):
    def get_object(self, feed_id):
        try: 
            return Feed.objects.get(id=feed_id)
        except Feed.DoesNotExist:    
            raise NotFound
    
    def get(self, request, feed_id):
        feed = self.get_object(feed_id)
        serialize = FeedSerializer(feed)
        return Response(serialize.data)
    