Django

# Django 단계 정리
1. Django 설치
2. Project 생성
3. App 생성
4. Model 정의
5. Migration 
6. 관리자 페이지 설정
7. View 설정
8. UR 설정
9. 서버 실행 및 확인
10. 템플릿 사용

# 폴더 구조

│ ├─ └─

```
├─db.sqlite3
├─manage.py
├─NOTEME.md
├─poetry.lock
├─pyproject.toml
├─.venv/
│   └─virtual env.
├─boards/
│   └─python apps
├─config/
│   └─python apps
├─feeds/
│   └─python apps
└─user/
    └─python apps
```

# 설치

```
poetry add Django # 라이브러리 설치
poetry shell # 가상환경 실행
django-admin startproject config . # 장고 프로젝트 생성
django-admin startapp myapp # 앱 생성
django-admin makemigrations
django-admin

```

추천

```
https://legend-palm-1f1.notion.site/04-Django-3-4-afc627b0a42b47c3b35967aee46a8d22
```

# URL & VIEW

## 파일로 따로 나누어 URL 관리

# Model

- Board > Table 개념
- Table

> DB에서 등록하려면 migration 해줘야함.
> makemigration > migrate : 사전 등록 > 완전 등록

orm 방식으로 사용하기

```
python manage.py shell
```

## model 만들 때 절차

1. 폴더 생성
2. config/setting에 등록
3. 코드 작성
4. admin.py 에 등록
5. migration, migrate

```
python manage.py startapp users
```

## Foreign KEY

```
콜럼이름 =  models.ForeignKey("부를 모델", 참조된 유저가 삭제되면 그 유저와 관련된 레코드도 삭제.)
user = models.ForeignKey("users.User", on_delete=models.CASCADE)
```
 
## REFERENCES
`https://legend-palm-1f1.notion.site/09-2-4-046fb212b1814589a9c88e222b4fbd32`

# Admin Panel
- 웹 애플리케이션의 데이터를 관리하기 위한 사용자 친화적인 인터페이스. (어드민 페이지)

1. 관리자 인터페이스 활성화
2. 모델을 관리자 페이지에 등록
3. 관리자 계정 생성
    - 생성
        `python manage.py createsuperuser` at zsh
4. 관리자 페이지 접속 및 사용    
5. 관리자 페이지 커스터마이징
    - Titling
        ```
        def __str__(self):
            return self.name
        ```
        at models.py
    - Categorizing 
        `list_display` at admin.py
    - Filtering
        `list_filter` at admin.py
    - Searching
        `search_field` at admin.py
    - Ordering
        `ordering` at admin.py
    - Readonly
        `readonly_fields` at admin.py
    - Detailing (fieldsets)
        ```
        filedsets = (
            (None, {'field': {'a', 'b'}}),
            ('Advanced options', {`field`:('x', 'y', 'z'), 'classes': ('colapse',)}),
        )
        
        ```

# Django User Model > 유저 정보 설정

- 장고 내에서 만들어 놓은 User Model이다. (여러가지 클래스가 담겨있어.)
- 비밀번호 해쉬화, 비밀번호 저장 등등의 기능의 다양한 기능

## 사용법

(0) users.app
```
python manage.py startapp users
```

(1) users/models.py 수정
```
from django.contrib.suth.models import AbstractUser

class User(AbsractUser)
    pass
```

(2) users/admin.py 
```
from django.contrb.auth.admin import UserAdmin

@admin.register(User)
class CustomerUserAdmin(UserAdmin):
    pass
```
(3) config/settings.py
```
AUTH_USER_MODEL = "user.User"
```

(4) users/migrations 폴더에서 00001,0002로 시작하는 파일 삭제 / db.sqlite3 삭제
(5) migrate
(6) user create
- db 초기화해서 해야함
```
python manage.py createsuperuser
```

# Django Common Model > 다양하게 사용 가능
- Logic: Common Model을 생성함으로써 공통으로 필요한 값을 만들어 놓고 그 안에 상속받을 Model을 따로 설정한다.
- CommonModel's Structure: 각 객체에 공통적으로 설정할 수 있는 정보(값) 
> ex) 만든 시각, 수정된 시각 등등 
- 이러한 값에 대한 app을 따로 설정하여 필요한 상황에 꺼내어 쓴다.

## 서순

1. common 예시 앱 생성
2. 상속
3. Migration
4. Custom Admin Panel 

## 코드
1. common 앱 생성
```
pyhton manage.py startapp common
```
2. 상속
상속해준다.
```
from common.models import CommonModel

class Chiren(CommonModel):
    ~~~
```
3. Migration
4. Custom Admin Panel 

## META
- DB 테이블에는 추가하지 않되, 추상 기반 class 저장하여 꺼낼 수 있다.
> model.py에 DB TABLE을 설정하지 않아도. 
> admin.py에서 쓸 수 있다는 의미.

# ORM (Object-Relational Mapping)
- Object (장고)
- Relatinal Datbase (RDBMS)
- Mapping

## 자주 사용하는 함수
1. filter()
    - 찾고 싶은 객체 반환
2. exclude()
    - 제외하고 싶은 객체 빼고 반환
3. annotate()
    - 쿼리 결과에 계산된 필드를 추가
4. aggregate()
    -  QuerySet에 포함된 객체들에 대해 집계연산 싫행 // 데이터베이스 단계에서 실행.
5. order_by()
    - 정렬
6. all()
    - 전체반환
7. get()
    - 데이터 반환, 값이 하나만 있어야함
8. exists()
    - 쿼리셋에 하나 이상의 객체가 존재하는 지에 대한 여부 확인
9. count()
    - 숫자 세기
10. select_related() / prefetch_related()
    - 관련된 객체를 효율적으로 불러오기 위한 메소드,
        - select_related() : JOIN을 사용하여 관련 객체를 한 번의 쿼리로 불러옴
        - prefetch_related() : 별도의 쿼리를 실행하여 관련 객체리르 미리 가져옴


## python manage.py shell
django 프로젝트에서 Python 인터프리터 환경을 Django와 연결하여 실행하는 명령어.
> Django ORM을 포함한 전체 프로젝트 환경에서 Python 코드를 실시간으로 실험하거나 실행할 수 있는 "개발용 콘솔"

```
python manage.py shell 
```

## ORM CRUD

### 기본 사용법
- model 불러오기
```
from board.models import Board // Board 테이블 가져오기
```

### CRUD
- 쿼리문 작성 

```
// Board 테이블 내에 id 값이 1인 쿼리 가져오기
board = Board.objects.get(id=1) 
```

```
// 제목 전부 불러오기
boards =  Board.objects.all() 
for i in boards:
    print(i.title)
```
### REVERSE ACCESSORS
- 역으로 데이터를 찾는 법. (부모 -> 자식 X;  자식 -> 부모 O)

```
from users.models import User

user = User.objects.get(pk=1) # pk가 1인 user를 가져옴
user.board => X 
    => user.board_set
board.user => O 

dir(user) # 이 함수를 통해서 user에서 사용가능한 모든 함수의 리스트를 본다.

BOARD => USER
USER <= BOARD (X)

user.board_set
user.board_set.all()
user.review_set

> user.board_set.all()
<QuerySet [<Board: 제목>, <Board: title2>, <Board: updated title>]>

```


## QUERY SET

- Django의 QuerySet은 데이터베이스의 데이터를 조회하고 필터링하는 데 사용되는 핵심 개념. 
- QuerySet = 테이블로부터의 객체 집합. 여러가지 방식으로 이 집합을 조직.

1. Lazy Excution
    - 천천히 불러와 데이터베이스의 부담을 지우기
    - 최대한 천천히 불러옴.
    - 사용할 때 바로 쿼리함.
2. Method Chaining
    - QuerySet의 메소드들을 연결하여 하나의 쿼리 문장을 만든다. (여러가지 쿼리를 하나의 쿼리를 묶는다.)
3. Main Methods
    - filter()
    - exclude()
    - annotate()
    - order_by()
    - all()
    - get()
4. Caching
    - 한번 사용한 QuerySet을 캐싱하여, 재사용 가능.
5. Slicing
    - 파이썬의 특정 부분만 추출 가능 / 인스타그램 피드 30개 제한처럼
6. Q / F Object 
    - Q 객체를 사용하여 복잡한 쿼리 조건 구성 가능
    ```
    from django.db.models import Q
    User.objects.filter(Q(is_staff=True) | Q(is_superuser=True))
    ```
    ```
    User.objects.filter(~Q(is_active=True))  # 비활성 유저 찾기
    ```
    - F 객체를 사용하여 필드 간의 관게나 조건 표현 가능.
    ```
    # 가격을 10% 올리기
    Product.objects.update(price=F('price') * 1.1)
    # views 수 1 증가
    Post.objects.filter(id=3).update(views=F('views') + 1)
    ```
| 항목     | Q 객체                           | F 객체                          |
| ------ | ------------------------------ | ----------------------------- |
| 목적     | 조건을 복합적으로 구성할 때 사용             | 필드 간의 비교나 연산을 할 때 사용          |
| 예시 용도  | OR / AND / NOT 조건 만들기          | stock < min\_stock 같은 비교      |
| 대표 메서드 | `filter()`, `exclude()` 등에서 사용 | `filter()`, `update()` 등에서 사용 
7. Database Optimization
    - 관련된 객체를 효율적으로 불러오기 위한 메소드,
    - select_related() : JOIN을 사용하여 관련 객체를 한 번의 쿼리로 불러옴
    - prefetch_related() : 별도의 쿼리를 실행하여 관련 객체를 미리 가져옴

    - **예시**:
    
    두 함수의 차이는 객체들을 불러오는 방식에 차이가 있습니다.
    
    **1. `select_related()` 사용 예시**
    
    - **상황**: "블로그 글"과 "작성자"가 있으며, 각 블로그 글은 하나의 작성자와 연결되어 있습니다.
    - **모델 구조**:
        
        ```python
        class Author(models.Model):
            name = models.CharField(max_length=100)
        
        class BlogPost(models.Model):
            title = models.CharField(max_length=100)
            content = models.TextField()
            author = models.ForeignKey(Author, on_delete=models.CASCADE)
        ```
        
    - **`select_related()` 사용**:
        
        ```python
        # BlogPost와 연관된 Author 객체를 한 번의 쿼리로 불러옵니다.
        posts = BlogPost.objects.select_related('author').all()
        
        for post in posts:
            print(post.title, post.author.name)
        ```
        
        여기서 **`select_related('author')`**는 BlogPost와 Author 테이블을 JOIN하여 한 번의 쿼리로 데이터를 가져옵니다. 이는 관련된 객체가 "하나"일 때 유용합니다.
        
    
    **2. `prefetch_related()` 사용 예시**
    
    - **상황**: "강사"와 "강의"가 있으며, 각 강사는 여러 강의를 진행할 수 있습니다.
    - **모델 구조**:
        
        ```python
        class Instructor(models.Model):
            name = models.CharField(max_length=100)
        
        class Course(models.Model):
            title = models.CharField(max_length=100)
            instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
        ```
        
    - **`prefetch_related()` 사용**:
        
        ```python
        # 각 Instructor에 연결된 모든 Course 객체를 별도의 쿼리로 미리 가져옵니다.
        instructors = Instructor.objects.prefetch_related('course_set').all()
        
        for instructor in instructors:
            print(instructor.name)
            for course in instructor.course_set.all():
                print(course.title)
        ```
        
        여기서 **`prefetch_related('course_set')`**는 Instructor와 연결된 모든 Course 객체를 별도의 쿼리로 가져온 후, Python에서 이를 조합합니다. 이는 관련된 객체가 "여럿"일 때 유용합니다.
        
        이러한 방식으로 **`select_related()`**와 **`prefetch_related()`**를 사용하면 데이터베이스의 부담을 줄이면서 필요한 데이터를 효과적으로 불러올 수 있습니다.


# RESET API

REST API (Respresentational State API)
- 자원을 이름으로 표현하여 자원의 상태를 주고 받는 것. (표현 방식: URI)

1. Django REST FRAMEWORK 설치
2. SEIRIALIZING
3. Serializing WorkFlow
4. Feeds/Users/Reviews 작성

### URI or URL?
URI > URL (Link)

## 1. Django REST frame 설치

(1) frame install
```
poetry shell
poetry add djangorestframework
```

(2) config/settings.py
```
INTALLED_APPS = [
    ...
    'rest_framework',
]
```

(3) INSTALLED_APPS 분리
```
INSTALLED_APPS = CUSTOMEDE_APPS + DJANGO_APPS
```

## 2. SERIALIZING
직렬화:  Django(Objects) -> JSON
역질렬화: JSON -> Django(Objects)

CLINET(REACT, VUE etc..) <-X-> DJango(Object)
    - 상호간 이해가 불가함.

### Serializer.py
- Serialzing Model Data 
- Serializer.py 클래스 생성후 ModelSerializer 상속.
```
# users/serializers.py
from rest_framework.serializers import ModelSerializer
from .models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__" # Model의 전체 field 가져옴
        fields = ("nickname", "email") # 원하는 특정 field만 가져옴
        exclude = ("password",) # 특정 field 제외 가능
```

### views.py

[views.py](http://views.py) ⇒ status에 따라서 처리 + Objects → JSON

- http 요청에 따라 get, post, put, delete 함수 실행됨.
- Objects 데이터 ⇒ Json 데이터로 직렬화하는 과정

```python
# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import Serializer

class Datas(APIView):
	def get(self, request):
		datas = Model.objects.all()
		serializer = Serializer(datas) # QuerySet이 2개 이상일 때 Object->JSON
		return Response(serializer.data) # serialized된 데이터를 return

	def post(self, request):
		data = request.data => JSON
		datas = Model.objects.create(Serializer(data)) # JSON->Objects

	def put(self, request):
		data = request.data => JSON
		datas = Model.objects.update(Serializer(data)) # JSON->Objects

	def delete(self, request):
		JSON => ID값 뽑아와서 
		data = Model.objects.get(id=id)
		data.delete()  # 객체 삭제 -> dir()
```

**urls.py**

- as_view() ⇒ APIVIew와 url을 맵핑시켜주는 함수

```python
from django.urls import path
from . import views

urlpatterns = [    
		path("", views.Models.as_view())
]
```

## Serializing WorkFlow
<strong> Model -> Serialzer -> View -> URL </strong>


## Feeds

### 3. GET/Feeds API (1/2)

---
### WorkProcess

- 1. app 및 model 생성
- 2. rest_framework 불러오기 in views.py
    - `from rest_framework.views import APIView`
        - CBV (Class Based View)
         - FBV (Function Based View)
- 3. views.py 작성
- 4. serializer 및 model 불러오기 
- 5. serializers.py 작성

```
class FeedSerializer(ModelSerializer):
    class Meta:
        model = Feed # Feed라는 모델이라는 직렬화 할 것이다.
        field = "__all__" # Feed의 모든 field를 직렬화 할 것이다.
``` 

6. serializer 불러오기 in views.py

7. views.py 작성 (2)

```
class Feeds(APIView):
    # 전체 게시글 조회
    def get(self,request):
        feeds = Feed.objects.all();

        # 객체 -> JSON (Serialize)
        serialized = FeedSerializer(feeds, many=True)

        return Response(serialized.data)
```
8. urls.py 작성 (해당 app 내)
    urlpatterns = [ 
        path("", views.Feeds.as_view()),
    ]

### 4. GET/Feeds API (2/2) 

1. 피드에서 유저 데이터도 불러옴
    - depth : 1
2. 유저 데이터에서 민감한 정보도 같이 불러와짐
3. 차단해야함
    - users/serializer.py
    - user = FeedUserrSerializer()

### 5. POST/Feeds API  

- 1. POST 작성 in views.py
```
def post(self, request):
    serializer = FeedSerializer(data=request.data) 
    feed = serializer.save(user = request.user) # 받은 데이터 저장 시, 유저 데이터도 받아야 함으로 넘겨줘야 함.
    serializer = FeedSerializer(feed)
    print("post serializer", serializer)

    return Response(serializer.data)
```

- 2. save() 함수 사용 시, is_valid() 함수로 먼저 확인해줘야함. (django가 그렇게 하래)
    - `serializer.is_valid()`  

## Users

### 6. POST/users API

- 1. password

- 2. other information towards users

### 7. UPDATE/users API

- 1. Get, Put 이용하기

```
class MyInfo(APIView):
    def get(self, request): 
        user = request.user 
        serializer = MyInfoSerializer(user)
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
```

- 2. 클래스 이용. 

- 3. 업데이트 설정 가능한 웹페이지 따로 생성하여 교체. # URL 설정

## Reviews

### 8. GET/ reviews API

models.py
```
from django.db import models
from common.models import CommonModel
# Create your models here.
class Review(CommonModel):  
    content = models.CharField(max_length= 100)
    likes = models.PositiveBigIntegerField(default=0)
    
    user = models.ForeignKey("users.User", on_delete=models.CASCADE) 
    feed = models.ForeignKey("feeds.Feed", on_delete=models.CASCADE)

```
serializers.py
```
from rest_framework.serializers import ModelSerializer
from .models import Review

class ReviewsSerializer(ModelSerializer):
    class Meta:
        model: Review
        fileds = "__all__" 
           
```
Views.py
```
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
```
urls.py
```
from django.urls import path
from . import views


urlpatterns = [
    path("", views.Reviews.as_view()),
    path("<int:review_id>/", views.ReviewDetail.as_view())
]
```

### 9. 유저 상세 데이터 받기 (ex, Feed 내에서 User_id를 통해 유저 데이터를 받았으면, id 값을 통해서 유저 닉네임 가져오는 것.)

1. User 정보를 담은 데이터 가져오기

- Serializer를 이용하여 user 데이터 가져오기
- (read_only로 보여주고 싶은 것 컨트롤 가능)

# Django Token AUTH

- Django에서 제공하는 TokenAUTH
1. Token AUTH 설정
2. 사용자 및 토큰 생성
3. API 뷰 생성

## AUTH TOKEN 설정
```
INSTALLED_APPS = [
	"rest_framework.authtoken" # 추가
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication', # 추가
    ],
}
```
zsh, cmd
```
python manage.py migrate 
```

## 사용자 및 토큰 생성 
> A. Django Sheell에서 토큰 활성화
> B. 토큰 적용
> C. 토큰 부여
    > 1. url 설정
    > 2. POSTMAN으로 확인
    > 3. /admin에서 토큰 확인

- Django Shell 활용
```
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

# settings.AUTH_USER_MODEL에 설정된 커스텀 유저 모델을 가져올 수 있습니다.
User = get_user_model()
user = User.objects.create_user('username', 'email@example.com', 'password') # 새로운 user 생성
token = Token.objects.create(user=user)
token.key
```

- 토큰 적용

```
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated 

...중략...
authentication_classes = [TokenAuthentication] # 토큰 적용
permissions_classes = [IsAuthenticated] # 권한 확인
```

- 토큰 부여 방법 
    - 1. url 설정
    - 2. POSTMAN으로 확인

1. url 설정
```
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("getToken", obtain_auth_token)
]
```
2. POSTMAN으로  확인
- 2.1 POSTMAN에서 아이디, 비밀번호를 통한 POST요청으로 TOKEN값 가져오기
```
{"username": "iwbb2020", "password":"plesasefuckingohome"}
```
- 2.2 HEADER에 GET요청에 TOKEN 값 담아서 보내기
<strong>HEADER</strong>
|Key|Value|
|---|---|
|Autrhorization|Authorization asd123dafg™¢adf|

3. /admin에서 토큰 확인

## 토큰 보안 관련 설정
1. HTTPS 사용
2. HTTP ONLY COOKIE
3. 토큰 만료 시간
4. 로컬 스토리지/ 세션 스토리지 사용
5. 토큰 분할
6. 보안환경에서 저장
7. 사용자 인터페이스 보호
8. 정기적인 토큰 갱신

## Django REST framework Overview

- DRF   
- 준비사항
- 프로젝트 및 앱 설정
- Serialization 모델 및 직렬화
- 뷰 및 URL 설정
- TokenAuthentication, IsAuthenticated  
- 주의사항 및 팁

# Django Session Login (Basic Login)

- Login
- Logout

## Login
- view 작성
    - username, password 정의
    - 누락 값 검사
    - 사용자 인증
``` 
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
            raise Response(status=status.HTTP_403_FORBIDDEN )
```

- url 등록
```
    path("login/", views.Login.as_view()),
```

## Logout
- view 작성
    - 로그인한 유저인지 확인
```
class Logout(APIView):
    # 로그인 했던 유저인지 확인
    permission_classes = [IsAuthenticated]
    def post(seslf, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)    
```
- url 작성 
```
    path("logout", views.Logout.as_view()),
```

# JWT 
REST-FRAMEWORK -> 유저마다 토큰 발행
SES SION -> 쿠키 탈취에 취약

JWT -> ACCESS와 FRESH토큰 두개 발행  

- A. CUSTOM JWT
- B. SIMPLE JWT

## A. CUSTOM JWT
- 1. 필요한 라이브러리 설치
- 2. Setting에서 Authentication Class 추가
- 3. 


### 1. 필요한 라이브러리 설치
```
pip install JWT # 로컬환경 설치 
poetry add JWT # 가상환경 설치
```
   
### 2. Setting에서 Authentication Class 추가
```
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.JWTAuthentication', # 추가
    ]
}  
```  
### 3. config/authentication.py 생성  
- ㄱ. JWT token 가져오기
- ㄴ. 토큰 디코딩 코드
```
from rest_framework.authentication import BaseAuthentication

class JWTauthentication():
    def authenticate(self, request):
        token = request.header.get("jwt-auth")

        if not token:
            return None
        
        jwt.decode
```

### 4. JWT 생성
- ㄱ. users/views.py
    - 1. JWT 토큰 생성
    - 2. 누락 값 검사
    - 3. 사용자 인증
    - 4. encode
```
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
            # encode 할 데이터 
            payload = {
                'id': user.id,
                'username': user.username,
            }
            # encode
            token = jwt.encode(
                payload=payload,
                jwt.settings.SECRET_KEY,
                algorithm='HS256'
            ) 
            return Response({'token': token})
```

- ㄴ. users/urls.py
```
urlpatterns = [
    path("login/jwt", views.JWTLogin.as_view())
]
```

### 5. API 인증
- ㄱ. users/views.py
```
from config.authentication import JWTAuthentication
class UserDetailView(APIView):
    authentication_classes = [JWTAuthentication] # 토큰 적용
    permisison_classes = [IsAuthenticated] # 권한   확인

    def get(self, request):
        user = request.user 
        return Response({"id":user.id, "username": user.usernames})
```
- ㄴ. users/urls.py
```
path('users/jwt/info', views.UserDetails.as_view())
```

## Differences with SimpleJWT
1. **수동 토큰 생성**:
    - 사용자가 제공한 자격 증명을 **`authenticate`** 함수로 검증합니다.
    - 유효한 자격 증명인 경우, **`jwt.encode`**를 사용하여 직접 JWT 토큰을 생성합니다.
    - 이 방식은 토큰의 구조와 내용을 완전히 제어할 수 있게 해줍니다.
    - 별도의 라이브러리(**`PyJWT`**)를 사용합니다.
2. **`django-rest-framework-simplejwt` 사용 (Simple JWT)**:
    - **`TokenObtainPairView`** 및 관련 뷰를 사용하여 자격 증명을 검증하고 토큰을 발급합니다.
    - 토큰 생성 및 검증 로직이 라이브러리에 내장되어 있어 복잡한 구현을 요구하지 않습니다.
    - 액세스 토큰과 리프레시 토큰을 자동으로 관리합니다.
    - **`django-rest-framework-simplejwt`** 설정을 통해 토큰 동작을 조정할 수 있습니다.

**사용 상황에 따른 선택**

- **Simple JWT 사용**: 토큰의 발급, 갱신, 검증 등의 기능을 손쉽게 구현하고 싶을 때 적합합니다. 또한 리프레시 토큰을 사용하여 보안성을 높이고 싶은 경우에도 좋습니다.
- **직접 토큰 생성**: 토큰의 내용이나 구조를 완전히 제어하고 싶거나, 특정 사용 사례에 맞춘 맞춤형 토큰이 필요한 경우에 적합합니다.

# SIMPLE JWT
- 기본 작업

## 1. 기본 작업
    - A. 설치
    - B. 앱 설정 

```
# 설치
pip install djangorestframework-simplejwt
poetry add djangorestframework-simplejwt
```

config/settings.py
```
# 앱 설정
"rest_framework_simplejwt,"


REST_FRAMEWORK = {
    "DEFAULT_AUTEHNTICATION_CLASSES": [
        "  "
    ]
}
```

## 2. JWT 인증 설정
자주 설정하는 JWT 설정
```
from datetime import timedelta
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=14),
    "SIGNING_KEY": "SECRET",
    "ALGORITHM": "HS256",
    "AUTH_HEADER_TYPES": ("Bearer",),
}
```


**`settings.py`**에서 Django REST framework의 기본 인증 설정을 JWT 인증으로 변경합니다.

- **설정값 예시**
    
    
    ```python
    from datetime import timedelta
    
    SIMPLE_JWT = {
    		# 액세스 토큰의 유효 기간을 5분으로 설정합니다.
        'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    	
        # 리프레시 토큰의 유효 기간을 1일로 설정합니다.
        'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
        
        # 리프레시 토큰을 갱신할 때마다 새 토큰을 생성하지 않도록 설정합니다.
        'ROTATE_REFRESH_TOKENS': False,  
    
        # 토큰을 갱신한 후 이전 토큰을 블랙리스트에 추가합니다.
        'BLACKLIST_AFTER_ROTATION': True,
    
        # JWT에 사용할 서명 알고리즘으로 HS256을 사용합니다.
        'ALGORITHM': 'HS256',
    
        # JWT를 서명하는 데 사용할 키로 Django의 SECRET_KEY를 사용합니다.
        'SIGNING_KEY': SECRET_KEY,
    
        # JWT 검증에 사용할 키입니다. HS256 알고리즘에서는 None으로 설정됩니다.
        'VERIFYING_KEY': None,  
    
        # 인증 헤더의 타입으로 'Bearer'를 사용합니다.
    		# Authorization: Bearer <token>
        'AUTH_HEADER_TYPES': ('Bearer',),
    
        # 토큰에 포함될 사용자 식별자 필드로 'id'를 사용합니다.
        'USER_ID_FIELD': 'id',  
    
        # 토큰 클레임에서 사용자 식별자에 해당하는 키로 'user_id'를 사용합니다.
        'USER_ID_CLAIM': 'user_id',  
    
        # 사용할 토큰 클래스로 AccessToken을 사용합니다.
        'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),  
    }
    ```
    
    - **`Bearer`**
        1. **표준 규약**: "Bearer" 용어는 OAuth 2.0 표준에서 정의되었으며, 토큰 기반 인증에서 널리 사용됩니다. 이 표준화된 접근 방식을 사용함으로써, 개발자들은 보편적으로 인정받는 방식을 따를 수 있으며, 다른 시스템과의 호환성을 유지할 수 있습니다.
        2. **명확한 의미 전달**: "Bearer"라는 단어는 토큰의 소지자가 해당 자원에 대한 액세스 권한을 가지고 있다는 것을 명확하게 전달합니다. 이는 다른 단어들보다 이 목적에 더 적합합니다.
        
        결론적으로, "Bearer"라는 용어는 토큰 기반 인증에서 널리 사용되고 인정받는 표준 용어이기 때문에 사용되고 있습니다.

- **ACCESS_TOKEN vs REFRESH_TOKEN**

    
    **액세스 토큰 (Access Token)**
    
    - **목적**: 사용자의 인증 정보를 담고, API 접근 권한을 부여하는 짧은 기간의 토큰입니다.
    - **유효 기간**: 일반적으로 짧게 설정됩니다 (예: 5분에서 1시간).
    - **보안**: 짧은 유효 기간으로 인해, 토큰이 탈취되더라도 공격자가 오랜 시간 동안 사용할 수 없습니다.
    
    **리프레시 토큰 (Refresh Token)**
    
    - **목적**: 액세스 토큰이 만료되었을 때 새로운 액세스 토큰을 발급받기 위해 사용하는 긴 기간의 토큰입니다.
    - **유효 기간**: 일반적으로 길게 설정됩니다 (예: 7일에서 30일). 이 예제에서는 14일로 설정되어 있습니다.
    - **보안**: 비교적 긴 유효 기간을 가지지만, 오직 새로운 액세스 토큰을 발급받는 용도로만 사용됩니다.
    
    **설계 팁**
    
    **1. 유효 기간의 균형**
    
    - **액세스 토큰**: 액세스 토큰은 짧은 유효 기간(예: 5분에서 1시간)을 가짐으로써, 탈취되더라도 제한된 시간 동안만 유효합니다. 이는 토큰이 노출되었을 경우의 위험을 줄여줍니다.
    - **리프레시 토큰**: 리프레시 토큰은 긴 유효 기간(예: 7일에서 30일)을 가짐으로써, 사용자가 자주 로그인을 반복하는 불편함을 줄여줍니다. 그러나 이는 동시에 토큰이 탈취될 위험을 증가시킬 수 있습니다.
    
    **2. 액세스 토큰 만료 시 리프레시**
    
    - 사용자가 계속해서 서비스를 이용하는 동안에는, 액세스 토큰이 만료되어도 자동으로 리프레시 토큰을 사용하여 새로운 액세스 토큰을 발급받을 수 있어야 합니다. 이를 위해 클라이언트 측 애플리케이션은 액세스 토큰의 만료를 감지하고, 필요 시 리프레시 토큰을 이용해 새 토큰을 요청하는 로직을 구현해야 합니다.
    
    **3. 리프레시 토큰의 안전한 저장**
    
    - 리프레시 토큰은 상대적으로 긴 유효 기간을 가지므로, 안전한 저장소에 보관되어야 합니다. 예를 들어, 서버 측에서는 데이터베이스에 안전하게 저장하고, 클라이언트 측에서는 적절하게 암호화된 형태로 로컬 저장소에 보관해야 합니다.
    
    **4. 리프레시 토큰의 재발급 고려**
    
    - 보안을 강화하기 위해, 리프레시 토큰을 사용할 때마다 새로운 리프레시 토큰을 발급하고, 이전 토큰은 무효화하는 것이 좋습니다. 이렇게 하면, 리프레시 토큰이 탈취되더라도 탈취자가 오랫동안 사용할 수 없게 됩니다.
    
    **5. 비정상적 접근 감지**
    
    - 서버는 토큰 사용 패턴을 모니터링하여 비정상적인 접근을 감지해야 합니다. 예를 들어, 짧은 시간 내에 여러 국가에서 동일한 토큰으로 요청이 들어오는 경우, 이는 토큰이 탈취되었을 가능성이 있습니다. 이런 경우에는 즉시 해당 토큰을 무효화하고, 사용자에게 경고를 보내어 추가 조치를 취하도록 해야 합니다.
    - **ACCESS_TOKEN과 REFRESH_TOKEN을 분리하는 이유**
        
        액세스 토큰과 리프레시 토큰을 분리하여 사용하는 이유
        
        1. **보안 강화를 위한 분리**: 액세스 토큰과 리프레시 토큰을 분리함으로써, 두 토큰이 각각 다른 목적으로 사용되고, 이에 따라 다른 보안 수준을 적용할 수 있습니다. 액세스 토큰은 짧은 유효 기간을 가지므로, 실제 리소스에 접근하는 데 사용되며, 만약 탈취되더라도 짧은 시간 동안만 유효합니다. 반면, 리프레시 토큰은 오랜 기간 동안 유효하지만, 오직 새로운 액세스 토큰을 발급받는 데만 사용됩니다.
        2. **성능과 효율성 향상**: 액세스 토큰은 상대적으로 짧은 유효 기간을 가지므로, 자주 갱신해야 합니다. 이는 서버에 부하를 줄이고, 사용자의 요청 처리 속도를 빠르게 하기 위한 선택입니다. 짧은 유효 기간의 액세스 토큰을 사용함으로써, 각 요청에 대한 인증 과정을 빠르게 처리할 수 있습니다.
        3. **세션 유지의 편의성**: 리프레시 토큰은 사용자가 자주 로그인을 반복하는 것을 방지합니다. 사용자가 서비스를 지속적으로 이용하는 동안에는, 리프레시 토큰을 사용해 자동으로 새로운 액세스 토큰을 발급받을 수 있어, 끊임없는 사용자 경험을 제공할 수 있습니다.
        4. **토큰 탈취에 대한 대응**: 액세스 토큰이 탈취되더라도, 그 피해는 짧은 유효 기간으로 인해 제한적입니다. 반면, 리프레시 토큰이 탈취되면 보다 심각한 문제가 발생할 수 있으나, 이를 방지하기 위한 여러 보안 조치를 취할 수 있습니다 (예: 안전한 저장, 사용 패턴 모니터링, 재발급 및 무효화 등).
        
        결국, 액세스 토큰과 리프레시 토큰의 분리는 보안과 성능, 그리고 사용자 경험을 모두 고려한 설계 결정입니다. 리프레시 토큰의 보안에 특별한 주의를 기울이면서, 이 두 가지 유형의 토큰을 효과적으로 사용하면, 보다 안전하고 효율적인 인증 시스템 구축을 할 수 있습니다.
        
    - **어쨌든 REFRESH_TOKEN이 털리면 끝 아니냐?**
        1. **리프레시 토큰의 안전한 저장**: 리프레시 토큰은 매우 중요하므로, 클라이언트 측에서는 이를 안전하게 저장하고 관리해야 합니다. 예를 들어, 웹 애플리케이션에서는 쿠키에 저장하는 대신, 보안이 강화된 저장소를 사용해야 합니다.
        2. **리프레시 토큰의 재발급 및 무효화**: 리프레시 토큰을 사용할 때마다 새로운 리프레시 토큰을 발급하고, 이전 토큰을 무효화하는 방법을 고려해야 합니다. 이렇게 하면, 토큰이 탈취되었다 하더라도, 공격자가 오랜 시간 동안 그 토큰을 사용할 수 없게 됩니다.
        3. **리프레시 토큰의 사용 패턴 모니터링**: 서버는 리프레시 토큰의 사용 패턴을 모니터링하여 비정상적인 행동을 감지해야 합니다. 예를 들어, 짧은 시간 내에 다수의 액세스 토큰 발급 요청이 발생한다면 이는 의심스러운 행동으로 간주될 수 있습니다.
        4. **리프레시 토큰의 활성화 구역 제한**: 가능하다면, 리프레시 토큰의 사용을 특정 지역이나 IP 주소로 제한하는 것도 좋은 방법입니다. 이를 통해 무단 접근을 효과적으로 방지할 수 있습니다.
        5. **두 단계 인증 (Two-Factor Authentication, 2FA)**: 보안을 더욱 강화하기 위해, 사용자 계정에 대한 두 단계 인증을 도입할 수 있습니다. 이렇게 하면, 공격자가 리프레시 토큰을 탈취했더라도 추가적인 인증 단계가 있어 무단 접근을 방지할 수 있습니다.

## 3. URL 설정

users/urls.py
```
from rest_framework_simple.jwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path("login/simpleJWT, TokenObtainPair View),
    path("login/simpleJWT/refresh, TokenRefreshView),
    path("login/simpleJWT/verify, TokenVerifyView)
]
```
### **TokenObtainPairView (`/login/simpleJWT`)**

- **사용 시점**: 사용자가 처음으로 로그인할 때 사용됩니다.
- **기능**: 사용자의 자격 증명 (사용자 이름과 비밀번호)을 받아서 검증하고, 유효하다면 액세스 토큰과 리프레시 토큰을 발급합니다.
- **프론트엔드 개발자의 역할**: 사용자가 로그인 폼을 통해 자격 증명을 제공하면, 이를 이 뷰에 전달하여 토큰 쌍을 받습니다.

### **TokenRefreshView (`/login/simpleJWT/refresh`)**

- **사용 시점**: 액세스 토큰이 만료되었을 때 사용됩니다.
- **기능**: 유효한 리프레시 토큰을 받아 새로운 액세스 토큰을 발급합니다.
- **프론트엔드 개발자의 역할**: 액세스 토큰이 만료되었음을 감지하면, 리프레시 토큰을 이 뷰에 전달하여 새로운 액세스 토큰을 받습니다.

### **TokenVerifyView (`/login/simpleJWT/verify`)**

- **사용 시점**: 토큰의 유효성을 검증할 필요가 있을 때 사용됩니다.
- **기능**: 제공된 액세스 토큰이 유효한지 검증합니다.
- **프론트엔드 개발자의 역할**: 토큰의 유효성을 확인하고 싶을 때 이 뷰를 사용할 수 있습니다.
- 위 함수들을 상속 받아 커스텀도 가능합니다.
    
    **`django-rest-framework-simplejwt`** 라이브러리는 **`TokenRefreshView`**와 **`TokenVerifyView`**를 이미 제공하므로 이들에 대한 별도의 view 함수를 작성할 필요는 없습니다. 그러나, 이러한 뷰의 작동 방식을 이해하고 사용자 정의를 하고 싶다면, 기본 뷰를 상속받아 확장할 수 있습니다.
    
    다음은 **`TokenRefreshView`**와 **`TokenVerifyView`**를 확장하는 방법을 보여주는 예시입니다:
    
### **TokenRefreshView 확장**
    
    ```python
    from rest_framework_simplejwt.views import TokenRefreshView
    from rest_framework.response import Response
    
    class CustomTokenRefreshView(TokenRefreshView):
        def post(self, request, *args, **kwargs):
            # 여기에서 커스텀 로직을 추가할 수 있습니다.
            # 예를 들어, 추가 로그 작성, 토큰 갱신 전/후 처리 등을 구현할 수 있습니다.
    
            # 부모 클래스의 post 메소드를 호출하여 기본 동작을 수행합니다.
            response = super().post(request, *args, **kwargs)
    
            # 추가 응답 데이터나 로직을 여기에 추가할 수 있습니다.
            # 예: response.data['custom_field'] = 'custom_value'
    
            return response
    ```
     
### **TokenVerifyView 확장**
    
    ```python
    from rest_framework_simplejwt.views import TokenVerifyView
    from rest_framework.response import Response
    
    class CustomTokenVerifyView(TokenVerifyView):
        def post(self, request, *args, **kwargs):
            # 여기에서 커스텀 로직을 추가할 수 있습니다.
            # 예를 들어, 토큰 검증 로그 작성, 추가 검증 로직 등을 구현할 수 있습니다.
    
            # 부모 클래스의 post 메소드를 호출하여 기본 동작을 수행합니다.
            response = super().post(request, *args, **kwargs)
    
            # 추가 응답 데이터나 로직을 여기에 추가할 수 있습니다.
            # 예: response.data['custom_message'] = 'Token is valid'
    
            return response
    ```
    
    이러한 커스텀 뷰를 사용하려면, Django의 URL 설정에서 기본 뷰 대신 이 커스텀 뷰를 사용해야 합니다:
    
    ```python
    from django.urls import path
    from .views import CustomTokenRefreshView, CustomTokenVerifyView
    
    urlpatterns = [
        # ...
        path('login/simpleJWT/refresh', CustomTokenRefreshView.as_view(), name='token_refresh'),
        path('login/simpleJWT/verify', CustomTokenVerifyView.as_view(), name='token_verify'),
    ]
    ```
    
    이 방법으로 **`django-rest-framework-simplejwt`**의 기본 동작에 추가적인 로직을 적용할 수 있습니다.


# TEST

# 59.TestCode(1/3)

## **Django REST Framework에서 API 테스트 작성하기**

1. **테스트 환경 설정**
2. **테스트 케이스 클래스 작성**
3. **setUp 메서드로 테스트 데이터 준비**
4. **API 테스트 메서드 작성**
5. **`reverse` 함수 사용하기**
6. **테스트 실행 및 결과 확인**

### 1. 테스트 환경 설정

먼저, Django REST framework 테스트 모듈을 임포트합니다. Django의 테스트 케이스와 **`status`** 모듈도 필요합니다. 이를 위해 다음과 같이 작성합니다:

```python
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
```

- **`APITestCase`:**
    - **`APITestCase`** 클래스는 Django의 **`TestCase`** 클래스를 확장하여 작성된 REST framework의 클래스입니다.
    - 이 클래스는 API 테스팅을 위한 추가적인 기능을 제공합니다. 예를 들어, 클라이언트 인스턴스를 포함하여 API 요청을 쉽게 보낼 수 있게 해주며, JSON과 같은 특정 콘텐츠 타입에 대한 지원을 추가합니다.
    - **`APITestCase`**를 사용하면 DRF(Django REST Framework) 기반의 API 엔드포인트를 테스트하는 데 필요한 환경을 쉽게 구성할 수 있습니다.
- **`status`:**
    - **`status`** 모듈은 HTTP 상태 코드를 나타내는 상수들을 포함하고 있습니다.
    - 예를 들어, **`status.HTTP_200_OK`**, **`status.HTTP_404_NOT_FOUND`**와 같이 의미 있는 이름으로 HTTP 상태 코드를 사용할 수 있게 해 줍니다.
    - 이러한 상수를 사용하면 코드의 가독성을 향상시키고, 직접 숫자를 입력하는 것보다 오류를 줄일 수 있습니다.
- **`reverse`:**
    - **`reverse`** 함수는 Django의 URL 관리 시스템의 일부입니다.
    - URL 패턴의 이름을 기반으로 해당 URL을 동적으로 생성해 줍니다.
    - 이 함수는 URL을 하드코딩하지 않고 URL 패턴의 이름을 사용하여 URL을 찾아내므로 URL 구조가 변경되어도 코드를 수정할 필요가 없게 해줍니다.
    - 예를 들어, **`reverse('predict_diabetes')`**는 'predict_diabetes'라는 이름의 URL 패턴에 매핑된 실제 URL 경로를 반환합니다.

### 2. 테스트 케이스 클래스 작성

테스트를 위한 클래스를 **`APITestCase`**로부터 상속받아 생성합니다. 이 클래스는 REST framework의 기능을 확장하여 API 테스트에 필요한 추가적인 기능을 제공합니다.

```python
class MyAPITestCase(APITestCase):
    pass  # 이곳에 테스트 메서드들을 작성
```

### 3. setUp 메서드로 테스트 데이터 준비

**`setUp`** 메서드는 각 테스트 메서드가 실행되기 전에 호출됩니다. 이곳에서 테스트에 필요한 사용자나 객체를 생성할 수 있습니다.

```python
def setUp(self):
    # 예시: 테스트용 사용자 생성
    self.user = User.objects.create_user(username='testuser', password='password')
```

### 4. API 테스트 메서드 작성

각 API 엔드포인트에 대해 하나씩 테스트 메서드를 작성합니다. 메서드 이름은 **`test_`**로 시작해야 합니다.

```python
def test_my_api_endpoint(self):
    # API 엔드포인트에 대한 테스트 코드 작성
    pass
```

### 5. **`reverse`** 함수 사용하기

URL을 하드코딩하는 대신, **`reverse`** 함수를 사용하여 URL을 동적으로 생성합니다. 이렇게 하면 URL 패턴이 변경되어도 테스트 코드를 수정할 필요가 없습니다.

```python
def test_my_api_endpoint(self):
    url = reverse('my_api_endpoint_name')
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
```

- path('api/', views.ViewName.as_view(), name='my_api_endpoint_name')

### 6. 테스트 실행 및 결과 확인

테스트를 실행하려면 Django의 **`python manage.py test`** 명령을 사용합니다. 각 테스트 메서드가 실행되고 결과가 콘솔에 출력됩니다.

```bash
python manage.py test
```

## Assert Function

Python의 **`unittest`** 프레임워크에는 다양한 **`assert`** 메서드들이 있으며, 각 메서드는 테스트 케이스에서 특정 조건을 검증하는 데 사용됩니다.

**1. `assertEqual` / `assertNotEqual`**

두 값이 같은지 또는 다른지 확인합니다.

```python
self.assertEqual(1 + 1, 2)  # 성공
self.assertNotEqual(1 + 1, 3)  # 성공
```

**2. `assertTrue` / `assertFalse`**

조건이 참(True)이거나 거짓(False)인지 확인합니다.

```python
self.assertTrue(1 + 1 == 2)  # 성공
self.assertFalse(1 + 1 == 3)  # 성공
```

**3. `assertRaises`**

특정 예외가 발생하는지 확인합니다.

```python
with self.assertRaises(ValueError):
    int("abc")  # ValueError 발생

# 범위를 벗어난 인덱스 접근 시 예외 발생
with self.assertRaises(IndexError):
    my_list = [1, 2, 3]
    print(my_list[3])  # 범위를 벗어난 인덱스

# 파일을 찾을 수 없을 때 예외 발생
with self.assertRaises(FileNotFoundError):
    open('nonexistentfile.txt')

# 잘못된 키 값 접근 시 예외 발생
with self.assertRaises(KeyError):
    my_dict = {'a': 1, 'b': 2}
    print(my_dict['c'])
```

**4. `assertIn` / `assertNotIn`**

항목이 주어진 시퀀스에 포함되어 있는지 확인합니다.

```python
self.assertIn(3, [1, 2, 3])  # 성공
self.assertNotIn(4, [1, 2, 3])  # 성공
```

**5. `assertIsNone` / `assertIsNotNone`**

값이 **`None`**인지 또는 **`None`**이 아닌지 확인합니다.

```python
self.assertIsNone(None)  # 성공
self.assertIsNotNone(1)  # 성공
```

**6. `assertAlmostEqual` / `assertNotAlmostEqual`**

두 부동 소수점 값이 거의 같은지 확인합니다.

```python
self.assertAlmostEqual(0.1 + 0.2, 0.3, places=1)  # 성공
self.assertNotAlmostEqual(0.1 + 0.2, 0.3, places=10)  # 성공
```

**7. `assertCountEqual`**

두 컨테이너가 동일한 요소를 동일한 개수만큼 포함하고 있는지 확인합니다.

```python
self.assertCountEqual([1, 2, 3], [3, 2, 1])  # 성공
```

**8. `assertDictEqual`**

두 딕셔너리가 동일한지 확인합니다.

```python
self.assertDictEqual({'a': 1, 'b': 2}, {'b': 2, 'a': 1})  # 성공
```

**9. `assertListEqual`**

두 리스트가 동일한지 확인합니다.

```python
self.assertListEqual([1, 2, 3], [1, 2, 3])  # 성공
```

**10. `assertSetEqual`**

두 세트가 동일한지 확인합니다.

```python
self.assertSetEqual({1, 2, 3}, {3, 2, 1})  # 성공
```

## 영상 실습 TestCode

feeds/urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.Feeds.as_view(), name="all_feeds"),
    path("<int:feed_id>", views.FeedDetail.as_view(), name="feed_detail"),
]
```

feeds/tests.py

```python
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Feed
from users.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class FeedAPITestCase(APITestCase):
    # 각 테스트 메서드가 실행되기 전에 호출
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        refresh = RefreshToken.for_user(self.user)
        self.token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")

        self.feed1 = Feed.objects.create(user=self.user, title="Title 1")
        self.feed1 = Feed.objects.create(user=self.user, title="Title 2")

    def test_get_all_feeds(self):
        url = reverse("all_feeds")
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 2)

    def test_get_feed_detail(self):
        url = reverse("feed_detail", kwargs={"feed_id": 1})
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data["content"], self.feed1.content)

    def test_create_feed(self):
        self.client.login(username="testuser", password="password")

        url = reverse("all_feeds")
        data = {"title": "New Title", "content": "New Feed"}
        res = self.client.post(url, data)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(
            Feed.objects.count(), 3
        )  # 전체 게시글의 갯수는 3개여야 합니다.
        self.assertEqual(Feed.objects.latest("id").content, "New Feed")
```

reviews/urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.Reviews.as_view(), name="reviews"),
    path("<int:review_id>", views.ReviewDetail.as_view(), name="review_detail"),
]
```

reviews/tests.py

```python
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Review
from users.models import User
from feeds.models import Feed
from rest_framework_simplejwt.tokens import RefreshToken

class ReviewAPITestCase(APITestCase):
    def setUp(self):
        # User Model
        self.user = User.objects.create_user(username="testuser", password="password")
        refresh = RefreshToken.for_user(self.user)

        self.token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")

        # Feed Model
        self.feed = Feed.objects.create(user=self.user, title="New Title")

        # Review Model
        self.review1 = Review.objects.create(
            content="Content 1", likes_num=0, user=self.user, feed=self.feed
        )
        self.review2 = Review.objects.create(
            content="Content 2", likes_num=0, user=self.user, feed=self.feed
        )

    def test_get_all_reviews(self):
        url = reverse("reviews")
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(Review.objects.count(), 2)

    def test_get_review_detail(self):
        url = reverse("review_detail", kwargs={"review_id": self.review1.id})
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data["content"], self.review1.content)
```

실행 시 `python manage.py test`

## Feed 모델의 test case

**`feeds/urls.py`**

```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.Feeds.as_view(), name='all_feeds'),
    path("<int:feed_id>", views.FeedDetail.as_view(), name='feed_detail')
]
```

**`feeds/tests.py`**

```python
from rest_framework.test import APITestCase # DRF
from rest_framework import status
from django.urls import reverse
from .models import Feed 
from users.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class FeedAPITestCase(APITestCase):
		# setUp 메서드는 각 테스트 메서드가 실행되기 전에 호출
    def setUp(self):
				# 테스트용 사용자에 대한 JWT 토큰 생성
        self.user = User.objects.create_user(username='testuser', password='password')
        refresh = RefreshToken.for_user(self.user)
        self.token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        self.feed1 = Feed.objects.create(user=self.user, content='Test Feed 1')
        self.feed2 = Feed.objects.create(user=self.user, content='Test Feed 2')

    def test_get_all_feeds(self):
        url = reverse('all_feeds')  # 'all_feeds'는 url 패턴 이름입니다.
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # 2개의 피드가 반환되어야 합니다.

    def test_get_feed_detail(self):
        url = reverse('feed_detail', kwargs={'feed_id': 1})  # 'user_feeds'는 url 패턴 이름입니다.
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
				self.assertEqual(res.data['content'], self.feed1.content)
        # self.assertEqual(len(response.data), 2)  # 해당 유저의 2개 피드가 반환되어야 합니다.
    
    def test_create_feed(self):
        self.client.login(username='testuser', password='password')
        url = reverse('all_feeds')  # 'feeds'는 URL 패턴 이름입니다.
        data = {'content': 'New Feed Content'}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Feed.objects.count(), 3)  # 게시글 수가 3개여야 합니다.
        self.assertEqual(Feed.objects.latest('id').content, 'New Feed Content')
		
		# 예시) view 생성 필요
    def test_delete_feed(self):
        self.client.login(username='testuser', password='password')
        url = reverse('feed_detail', kwargs={'feed_id': self.feed1.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Feed.objects.count(), 1)

    def test_update_feed(self):
        self.client.login(username='testuser', password='password')
        url = reverse('feed_detail', kwargs={'feed_id': self.feed1.id})
        data = {'content': 'Updated Content'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.feed1.refresh_from_db()
        self.assertEqual(self.feed1.content, 'Updated Content')

    def test_unauthorized_access(self):
        url = reverse('all_feeds')
        data = {'content': 'Should Not Create'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_feed_detail(self):
        url = reverse('feed_detail', kwargs={'feed_id': self.feed1.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['content'], self.feed1.content)

    def test_invalid_input(self):
        self.client.login(username='testuser', password='password')
        url = reverse('all_feeds')
        data = {'wrong_field': 'Invalid Data'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
```

- **`reverse`를 테스트에서 사용하는 예시**
    
    Django REST framework에서 API 테스트를 작성할 때 **`reverse`** 함수는 API 엔드포인트의 URL을 생성하는 데 유용합니다.
    
    **urls.py**
    
    ```python
    from django.urls import path
    from . import views
    
    urlpatterns = [
        path("", views.Feeds.as_view(), name='all_feeds'),
        path("<int:feed_id>", views.FeedDetail.as_view(), name='user_feeds')
    ]
    ```
    
    **tests.py**
    
    ```python
    from django.urls import reverse
    
    # 전체 피드를 가져오는 URL
    url_all_feeds = reverse('all_feeds')
    
    # 특정 사용자의 피드를 가져오는 URL
    url_user_feeds = reverse('user_feeds', kwargs={'username': 'testuser'})
    ```
    
    이렇게 하면, 실제 URL 경로를 직접 코딩할 필요 없이 URL을 동적으로 생성할 수 있으며, URL 패턴이 변경되어도 테스트 코드를 수정할 필요가 없습니다.
    

## Review 모델의  test case

**urls.py**

```python
from django.urls import path
from . import views

urlpatterns = [
    path("/", views.Reviews.as_view(), name='reviews'),
    path("/<int:review_id>/", views.ReivewDetail.as_view(), name='review_detail')
]
```

**tests.py**

```python
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import Review 
from users.models import User
from feeds.models import Feed
from rest_framework_simplejwt.tokens import RefreshToken

class ReviewAPITestCase(APITestCase):
    def setUp(self):
        # 테스트용 유저와 피드 생성        
				self.user = User.objects.create_user(username='testuser', password='password')
        refresh = RefreshToken.for_user(self.user)
        self.token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')       
				self.feed = Feed.objects.create(user=self.user, content='Test Feed')

        # 테스트용 리뷰 생성
        self.review1 = Review.objects.create(content='Content 1', likes_num=0, user=self.user, feed=self.feed)
        self.review2 = Review.objects.create(content='Content 2', likes_num=0, user=self.user, feed=self.feed)

    def test_get_all_reviews(self):
        url = reverse('reviews')
        res = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Review.objects.count(), 2)

    def test_get_review_detail(self):
        url = reverse('review_detail', kwargs={'review_id': self.review1.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['content'], self.review1.content)  # 리뷰 내용 확인
```

### **테스트 메서드 설명:**

- **`test_get_all_reviews`**: 모든 리뷰를 가져오는 API를 테스트합니다. **`reviews`** URL을 사용하여 GET 요청을 보내고, 응답 코드와 반환된 데이터의 길이를 확인합니다.
- **`test_get_review_detail`**: 단일 리뷰 상세 정보를 가져오는 API를 테스트합니다. **`review_detail`** URL에 리뷰 ID를 전달하여 GET 요청을 보내고, 응답 코드와 반환된 리뷰 데이터의 제목을 확인합니다.

