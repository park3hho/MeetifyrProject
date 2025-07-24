from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ParseError  
from .serializers import MyInfoSerializer, FeedUserSerializer
from django.contrib.auth.password_validation import validate_password

from rest_framework.authentication import TokenAuthentication # 사용자 인증
from rest_framework.permissions import IsAuthenticated # 권한 부여
from django.contrib.auth import authenticate, login, logout
from rest_framework import status

# Create your views here.
class Users(APIView):
    def get(self, request):
        user  = request.data
        serializer = MyInfoSerializer(user, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        password = request.data.get('password')
        serializer = MyInfoSerializer(data=request.data)
        
        # 비밀번호 유효성 검사
        try: 
            validate_password(password)
        except:
            raise ParseError("Invalid one")

        # 데이터 유효성 검사
        if serializer.is_valid():
            user = serializer.save() #새로운 유저 생성
            user.set_password(password) #비밀번호 해쉬화
            user.save() #  

            serializer = MyInfoSerializer(user)
            return Response(serializer.data)
        else:
            raise ParseError(serializer.errors)

# Get, Put를 이용하여 업데이트 할 수 있게 만드는 Class
class MyInfo(APIView):
    authentication_classes = [TokenAuthentication] 
    permission_classes = [IsAuthenticated]


    def get(self, request): 
        user = request.user 
        serializer = FeedUserSerializer(user)
        return Response(serializer.data)
    
    def put(self, request):
        user = request.user
        serializer = MyInfoSerializer(user, data=request.data, partail=True)
        
        if serializer.is_valid():
            user = serializer.save()  
            serializer = MyInfoSerializer(user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

# Login   
class Login(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # 누락 값 검사
        if not username or not password:
            raise ParseError()
        
        # 사용자 인증,
        user = authenticate(request, username=username, password=password)

        if user: 
            login(request, user)
            return Response(status=status.HTTP_200_OK)
        else:
            raise Response(status=status.HTTP_403_FORBIDDEN)
        
# Logout
class Logout(APIView):
    # 로그인 했던 유저인지 확인
    permission_classes = [IsAuthenticated]
    def post(seslf, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)

# JWT TOKEN 생성
import jwt
from django.conf import settings #  Secret Key 가져오기
class JWTLogin(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        # 누락 값 검사
        if not username or not password:
            raise ParseError()
        
        # 사용자 인증
        user = authenticate(request, username=username, password=password)
        if user:
            payload = {
                'id': user.id,
                'username': user.username,
            }
            token = jwt.encode(
                payload,
                settings.SECRET_KEY,
                algorithm='HS256'
            ) 
            return Response({'token': token})
        
# JWT API 인증
from config.authentication import JWTAuthentication
class UserDetailView(APIView):
    # authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({"id": user.id, "username": user.username} )