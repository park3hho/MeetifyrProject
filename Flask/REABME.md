Flask

# 특징

    확장가능성이 높다
    실전용은 낮다. MVP 개발용도

# 풀스택 프레임워크 VS 마이크로 프레임워크

    풀스택
        전체적인 애플리케이션에 필요한 모든 것을 포괄적으로 제공하는 프레임워크
        기능의 포괄성
        내부 일괄성
        1. Java Spring
        2. Python Django
        3. Ruby on Rails
    마이크로
        기능에 중점, 선택적으로 추가한다.
        경량성
        유연성
        1. Flask
        2. Express.js (Node.js)
            비동기 프로그램이 장점

# Flask 프로젝트 세팅

    프로젝트 폴더 생성
    가상환경 생성
        poetry (django)
            Python -m venv .venv
        conda
        venv
    flask 모듈 설치
    app.py 생성
    flask 실행
        flask run

# 라우팅

서버의 사용
flask run 개발환경에서 사용
WSGI 배포단계에서 사용

    사용
        기본경로 설정

    Jinja(Template Engine)
        동적 데이터 렌더링

        {% ... %}
            제어 구조
            반복문

# REST API (Representational State Transfer Application Programming Interface)

자원(Resources, 데이터) 중심으로 설계

프로토콜 메소드를 통해 자원에 대한 작업을 수행함.

> **자원 식별**: 사용자 정보 자원은 `/users/{userId}`URI를 통해 식별 <br/> > **자원 표현**: 사용자 정보는 JSON, XML의 형태로 클라이언트에게 전달 <br/> > **자원에 대한 행위**: 사용자 정보를 조회하기 위해 `GET /users/{usrId}`요청을 사용하고 , 사용자를 생성하기 위해 POST `/users`요청을 사용

CRUD(Resources) => PGPD(Protocol Methods)

## API의 구성 요소

> (1) 자원(resource): URI <br/>
> 클라는 위와 같은 URI 형식을 통해 서버에 데이터를 요청 <br/><br/>
> (2) 행위(methods, status): <br/>1. GET <br/>2.POST<br/> 3. PUT<br/> 4. DELETE</li><br/><br/>
> (3) 표현(representation):<br/>서버에서 클라로의 데이터 전달 방법 (`xml`, `json`, `txt`, `rss`)

## 원칙

- (1) 자원 기반의 URL <br/>
- (2) statelessness
  - 독립적인 요청: 각 API 요청은 다른 요청과 독립적으로 처리됨. 서버는 요청에 대한 정보를 기억하지 않음.
  - 서버의 상태 저장 없음: 서버에 이전 행동에 관한 정보를 저장하지 않음. 모든 요청은 필요한 모든 정보를 포함해야함. `(사용자 인증 정보)`
  - 세션 관리의 부재: 세션 상태`(로그인 상태, 이전 작업 등)`를 기억하거나 관리하지 않음
- (3) 표준화된 메소드 사용
- (4) Representation

## REST API 해석 연습

### 1.

- feeds/1

  - GET: id가 1인 게시글 데이터 보내줘
  - POST: id가 1인 게시글 만들어줘
  - PUT: id가 1인 게시글 수정해줘
  - DELETE: 1번 게시글 삭제해줘

- feeds/all

  - GET: 게시글 데이터 전부 보내줘
  - POST: X
  - PUT: X
  - DELETE: X

- myinfo

  - GET: 내 정보 보여줘
  - POST: X
  - PUT: 내 정보 수정
  - DELETE: 회원탈퇴

- users/1
  - GET: 1번 유저의 정보

### 2. 인스타그램 API

| 작업               | 메소드 | URL                       | 설명                      |
| ------------------ | ------ | ------------------------- | ------------------------- |
| 사용자 프로필 조회 | GET    | /users/{username}         | 사용자 프로필 정보를 조회 |
| 게시물 목록 조회   | GET    | /posts                    | 모든 게시물 조회          |
| 새 게시물 작성     | POST   | /posts                    | 새로운 게시물 작성        |
| 게시물 수정        | PUT    | /posts/{posts_id}         | 게시물 수정               |
| 게시물 삭제        | DELETE | /posts/{posts_id}         | 게시물 삭제               |
| 댓글 목록 조회     | GET    | /posts/{post_id}/commnets | 게시물 댓글 조회          |
| 댓글 작성          | POST   | /posts/{post_id}/commnets | 게시물 댓글 작성          |
| 팔로우             | POST   | /user/{user_id}/follow    | 사용자 팔로우             |
| 언팔로우           | DELETE | /user/{user_id}/follow    | 사용자 언팔로우           |

# JSONIFY

- Python 데이터를 JSON 형식으로 변환하여 HTTP응답으로 반환하는 함수
- Python의 기본 데이터 타입(딕셔너리, 리스트)를 JSON 문자열로 변화
- JSON (JavaScript Object Notion)
  - Key, Value 형태
  - 컴퓨터간 상호작용의 형식

## 1. Library Import

```
from flask import request, jsonify
```

## 2. GET Method

```
@app.route('/api/v1/feeds', methods=['GET'])
def get_all_feeds():
    data={'result': 'success', 'feeds': ['feed1', 'feed2', 'feed3']}
    return jsonify(data)
```

## 3. POST Method

POSTMAN 설치

```
@app.route('/api/v1/feeds', methods=['POST'])
def create_feed():
    name = request.form['name']
    age = request.form['age']

    print(name, age)

    return jsonify({'result': 'success'})
```

```
request.get_json() #들어오는 데이터는 json형태로 받겠다.
```

### 에러

```
400 Bad request. The browser (or proxy) sent a request that this server could not understand.
```

- POST parmeter 없을 시 발생
- 제대로 된 param(BODY)에 보냈는지 확인

`출처: https://skylit.tistory.com/316 [초코아빠*:티스토리]`

# Flask-RESTfulAPI

## Flask-RESTfulAPI 설치

```
pip install flask-restful
from flask_restful import Resource
```

## 사용예시

/resources/item.py

```
class Item(Resource):
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item
        return {"msg": "Item not found"}, 40
```

app.py

```
from flask_restful import Api
from resources.item import Item

api = Api(app)

api.add_resource(Item, '/item/<string:name>') # add default route
```

# smorest

- REST API를 쉽게 작성할 수 있도록 도와주는 라이브러리
- Flask-REST보다 더 많은 기능과 OpenAI(Swagger)문서 자동 생성 기능을제공

## smorest 설치

```
pip install flask-smorest
```

## flask app 진입점

```
from flask import Flask
from flask_smorest import Api
from api import blp

app = Flask(__name__)

# OpenAPI 관련 설정

app.config["API_TITLE"] = "My API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.1.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui" #페이지를 예뻐보이게 하는 기능

app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)
api.register_blueprint(blp)

if __name__ == "__main__":
    app.run(debug=True)
```

## Schemas 설정

`pip3 install marshmallow`

```
from marshmallow import Schema, fields
# marshmallow 라는 모듈에서 Schema와 fields를 불러옴

class ItemSchema(Schema)
# 클래스명을 ItemSchema 라고 하고 marshmallo 에서의 Schema를 상속받음

    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str()
    # 위 세 줄의 형태를 객체라고 하며, 이 객체를 나중에 직렬화하거나
    역직렬화할 때 실제로 거기에 데이터에서 뭔가 잘못된 것이 있는지 체크해줌
```

## Blueprint

- 블루프린트는 애플리케이션의 특정 기능 별로 라우팅, 뷰 함수, 템플릿, 정적 파일 등의 관리가 가능
  - API가 복잡해질 수록 관리의 필요성이 증가함.

주요 기능:

- 모듈화
- 라우팅 관리: 블루프린트의 자체 URL 규칙
- 기능별 분리: 블루프린트 특정 기능에 대한 라우팅, 뷰 함수, 에러 핸들러, 템플릿 등등

사용법:

- 블루프린트 구문 작성
- 앱에 블루프린트 등록

```
from flask import Flask, Blueprint, render_template, request

app = Flask(__name__)

# 첫 번째 블루프린트
my_blueprint = Blueprint('my_blueprint', __name__)

@my_blueprint.route('/hello')
def hello():
    return "Hello from my blueprint!"

@my_blueprint.route('/greet/<name>')
def greet(name):
    return f"Hello, {name}!"

# 두 번째 블루프린트
another_blueprint = Blueprint('another_blueprint', __name__, url_prefix='/another')

# /another/world
@another_blueprint.route('/world')
def world():
    return "Hello, world, from another blueprint!"

# /another/echo
@another_blueprint.route('/echo', methods=['POST'])
def echo():
    data = request.json
    return f"Received: {data}"

# 블루프린트에 템플릿을 사용하는 예제
@another_blueprint.route('/template')
def using_template():
    return render_template('example.html')

# 세 번째 블루프린트
third_blueprint = Blueprint('third_blueprint', __name__, url_prefix='/third')

@third_blueprint.route('/bye')
def goodbye():
    return "Goodbye from the third blueprint!"

# 애플리케이션에 블루프린트 등록
app.register_blueprint(my_blueprint)
app.register_blueprint(another_blueprint)
app.register_blueprint(third_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
```

## Abort

- 기능
  - API 개발 중 오류 처리
  - 오류 상태와 메세지 전달
- Flask와 Flask-smorest에서 함수 처리 요청 중 오류가 발생 했을 때 사용됨.

### 기본 사용법

```
from flask_smorest import abort

# 오류 상황에서 abort 호출
abort(404, message = "Resource not found")
```

```
from flask import Flask, abort

app = Flask(__name__)

@app.route('/example')
def example():
    error_condition = True

    # 어떠한 조건에서 오류를 발생시키고 처리
    if error_condition:
        abort(500, description = "An error occurred while processing the request.")

    # 정상적인 응답
    return "Success"
```

# flask-MySQL (DB)

### 필요한 도구

- Flask
- MySQL
- MySQL Workbench
- Flash-MySQL-DB

설치: Cloud Service DB의 경우 경로만 바꾸어주면 OK~.

## flask MysQL 설치

`pip install flask-mysqldb`

## tabel(MySQL) 생성 및 DB관련 코드(app.py) 작성

MySQL

```
CREATE DATABASE oz;
USE oz;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);
```

app.py

```
from flask import Flask
from flask_mysqldb import MySQL
from flask_smorest import Api
# user_routes에서 Blueprint 직접 임포트 대신 함수 임포트
from user_routes import create_user_blueprint

app = Flask(__name__)

# MySQL 연결 설정
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'oz-password'
app.config['MYSQL_DB'] = 'oz'

mysql = MySQL(app)

# blueprint 생성 및 등록
app.config["API_TITLE"] = "My API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.1.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

user_blp = create_user_blueprint(mysql)
api = Api(app)
api.register_blueprint(user_blp)


from flask import render_template
@app.route('/users_interface')
def users_interface():
    return render_template('users.html')


if __name__ == '__main__':
    app.run(debug=True)
```

## Error

클래스 내의 어트리뷰트가 없음.

`'NoneType' object has no attribute 'name'`

# ORM (Flask-SQLAlchemy / DB)

- 파이썬의 객체 관계 매핑 (Object Relational Mapping)
  - SQL이 아닌 ORM 방식으로 DB의 데이터를 조회할 수 있도록 도와줌.

## ORM (Object-Relational Mapping)

객체 : 객체, 클래스, 속성의 구조
관계형 데이터 베이스: 테이블 로우 컬럼과 같은 구조

- 데이터베이스의 테이블을 객체로 매핑하고, 객체 간의 관계를 데이터베이스의 외래 키 등으로 매핑하는 방식
- 객체 - Python(Flask, Django)
- Relational DataBase
- 위 두 가지를 Mapping 시키는 것
  => DB에 있는 데이터들을 객체처럼 사용할 수 있도록 도와줌. SQL 쿼리문 없이 데이터 CRUD가 가능.

기능

1. Model

- DB 테이블 생성을 해줌

2. ORM

- DB 테이블 데이터를 읽음

WHY ORM??

- 데이터베이스 코드가 간결해짐
- 결과 오류를 줄임 (쿼리에 대한 증명이 가능 > Schema)
- 쿼리를 쉽게 작성할 수 있음 (진입장벽 넘어가면 쉬움.)

## Flask-SQLAlchemy

- Flask에서 SQLAlchemy(ORM)을 사용할 수 있도록 도와주는 라이브러리

## 설치 목록

라이브러리 설치 / Flask-sqlAlchemy

```
pip install Flask-sqlAlchemy
pip install pymysql #connect with mysql through sqlAlchemy
```

## 파일 구조 구축

```
│ ├ └ ─

├─app.py
├─db.py
├─models.py
└─routes
    ├─users.py
    └─board.py
```

- app.py
  - 구동하는 코드 작성
- moedels.py
  - 스키마 작성
    - `boards = db.relationship('Board', back_populates='author', lazy='dynamic') `
      - 상호참조(역참조),
      - lazy='dynamic'설정(lazy=dynamic 이 쿼리셋은 데이터 베이스에서 즉시 모든 데이터를 로딩하지 않음. 일부만 로딩하려할 때 유용하다. 사용자가 작성한 게시판 글들의 목록을 관리할 때, 한번에 모든 글을 로드하지 않고 필요에 따라 특정 글들만 조회할 수 있도록 한다.)

## python 작성

## html 작성

- /templates 작성
- 그 안에 html 만들기
  - /templates/boards.html
  - /tempaltes/users.html

app.py

```
from flask import Flask
from flask_smorest import Api
from db import db
from models import User, Board

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:As583346!@@127.0.0.1/oz' #MySQL 연결
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #추적 기능 비활성화

db.init_app(app)  # db 객체를 Flask 앱에 연결, db객체는 중복 사용하므로 모듈화

#blueprint 설정
app.config['API_TITLE'] = 'My API'
app.config['API_VERSION'] = 'v1'
app.config['OPENAPI_VERSION'] = '3.1.3'
app.config['OPENAPI_URL_PREFIX'] = '/'  # OpenAPI URL 접두사 설정
app.config['OPENAPI_SWAGGER_UI_PATH'] = '/swagger-ui'  # Swagger UI 경로 설정
app.config['OPENAPI_SWAGGER_UI_URL'] = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/'  # Swagger UI 리소스 URL

api = Api(app)  # Api 객체 생성

from flask import render_template # 라우팅
@app.route('/manage-boards')
def manage_board():
    return render_template('boards.html')

@app.route('/manage-users')
def manage_users():
    return render_template('users.html')

if __name__ == '__main__':
    with app.app_context():
        print("main run")
        db.create_all()

    app.run(debug=True)
```

model.py

```
# Model -> Table
# 게시글 - board
# 유저 - user
# 추후 모델들을 models/user.py models 디렉토리를 만들어 관리하는 것이 좋음.
from db import db

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    boards = db.relationship('Board', back_populates='author', lazy='dynamic')
    #역참조 개념, 사용자가 작성한 모든 게시물을 나타냄 ()
    #lazy=dynamic 이 쿼리셋은 데이터베이스에서 즉시 모든 데이터를 로딩하지 않음.
    #일부만 로딩할 때 유용함. 사용자가 작성한 게시판 글들의 목록을 관리할 때,
    #한번에 모든 글을 로드하지 않고 필요에 따라 특정 글들만 조회할 수 있도록 함.

class Board(db.Model):
    __tablename__ = "boards"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    author = db.relationship('User', back_populates='boards')
    #역참조, 게시물 작성한 사용자(user)를 나타냄.
```

board.py

```
from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint
from db import db
from models import Board

board_blp = Blueprint('Boards', 'boards', description='Operations on boards', url_prefix='/board')



# id 값이 필요한지 아닌지에 대한 유무
@board_blp.route('/')
class BoardList(MethodView):
    def get(self): # 모든 게시글 불러오기
        boards = Board.query.all() # Board의 모든 데이터 가져옴.
        return jsonify([{"user_id": board.user_id,
                        "id": board.id,
                        "title": board.title, "content": board.content, "author": board.author.name} for board in boards])

    def post(self): # 게시글 만들기
        data = request.json # 데이터는 json 형태로 받음
        new_board = Board(title=data['title'], content=data['content'], user_id=data['user_id'])
        # 데이터베이스에 추가하기 위한 {key:value} 형태로 변환
        db.session.add(new_board) # 데이터 베이스에 추가
        db.session.commit()
        return jsonify({"message": "Board created"}), 201

#
@board_blp.route('/<int:board_id>')
class BoardResource(MethodView):
    def get(self, board_id): #(self, board_id)
        board = Board.query.get_or_404(board_id)
        #id값으로 얻어야 하기에 Board.query.all() -> Board.query.get_or_404(board_id)로 가져옴
        return jsonify({"title": board.title, "content": board.content, "author": board.author.name})

    def put(self, board_id): #업데이트한데용~
        board = Board.query.get_or_404(board_id)
        data = request.json
        board.title = data['title'] #title과 content만 바꿈
        board.content = data['content']
        db.session.commit()
        return jsonify({"message": "Board updated"})

    def delete(self, board_id):
        board = Board.query.get_or_404(board_id)
        db.session.delete(board)
        db.session.commit()
        return jsonify({"message": "Board deleted"})
```

users.py

```
from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint
#블루프린트는 애플리케이션의 특정 기능 별로 라우팅, 뷰 함수, 템플릿, 정적 파일 등의 관리가 가능
from db import db
from models import User

user_blp = Blueprint('Users', 'users', description='Operations on users', url_prefix='/users')

@user_blp.route('/') #유저의 id가 필요 없기에 '/' 사용
class UserList(MethodView):
    def get(self): # 유저를 전부 가져옴.
        users = User.query.all() # 전부 주세여~
        user_data = [{"id":user.id, "name": user.name, "email": user.email} for user in users]  # Convert to list
        return jsonify(user_data)

    def post(self):
        print("요청은 오는가?")
        user_data = request.json # request.json -> 유저가 보낸 데이터
        new_user = User(name=user_data['name'], email=user_data['email'])
        # key:value로 나누기, 데이터 형식 구분
        db.session.add(new_user) # 데이터베이스에 추가
        db.session.commit()
        return jsonify({"message": "User created"}), 201

@user_blp.route('/<int:user_id>') # id값이 필요
class Users(MethodView):
    def get(self, user_id): # self, user_id
        user = User.query.get_or_404(user_id) # 하나만 조회 -> get_or_404(user_id) 사용
        return {"name": user.name, 'email': user.email}

    def put(self, user_id): # 업데이트
        user = User.query.get_or_404(user_id)
        user_data = request.json

        # update 항목
        user.name = user_data['name']
        user.email = user_data['email']

        db.session.commit()
        return {"message": "User updated"}

    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return {"message": "User deleted"}
```

## 에러

`Errno 11003` > SQLAlchemy 1.4를 사용하면 해결됨.

- 1. SQL Alchemy 1.4 사용
- 2. MySQL80 서비스 실행
- 3. 해결 못해서 MySQL 삭제 해버림

# db 객체 모델 정의 방법 2가지

## db 객체와 모델 클래스를 같은 파일에 위치시키기

models.py

```
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    #... User model

Class Board(db.Board):
    # ... Board model
```

app.py

```
db.init
```

## db 객체와 모델 클래스를 분리하기 (모델이 많아져서 관리해야할 시)

db.py

```
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy
```

model.py

```
from db import db

class User(db.Model):
    # User Model

class Board(db.Model):
    # Board Model
```

app.py

```
db.init_app(app)
```

# Schema와 Model의 차이

| 이름   | 정의                                                                    | 용도                           |
| ------ | ----------------------------------------------------------------------- | ------------------------------ |
| Schema | 데이터의 직렬화와 역직렬화, 유효성 검증을 위해 사용됨                   | 직렬화,역직렬화에 초점         |
| Model  | 데이터베이스의 테이블을 의미함, ORM 도구를 통해 데이터베이스와 상호작용 | 데이터베이스와 상호작용에 초점 |

## 직렬화와 역직렬화 (Schema의 주요 용도)

### 직렬화(Serialization)

복잡한 데이터 구조를 JSON과 같은 포맷으로 변환하는 과정

```
# Python Data
user_instance = User(id=1, username='JohnDoe')

# Serialization
class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str()

# Result
{
    "id": 1,
    "username": "JohnDoe"
}
```

### 역직렬화(Deserialization)

JSON 데이터를 Python과 같은 데이터 구조로 바꾸는 것

```
# JSON Data
{
    "username": "JaneDoe"
}

# Deserialization
user_data = {"username": "JaneDoe"}
user_schema = UserSchema()
user_instance = user_Schema.load(user_data)

# Result
User(username='JaneDoe')
```

# Flask-Migrate

- 데이터베이스의 변화를 알려주는 라이브러리 (Django는 장착되어 있음)
- Alembic: SQLAlchemy 사용 시에 데이터베이스를 관리해주는 Python기반의 마이그레이션 도구.
  - 데이터베이스 스키마 변경 감지
  - 데이터베이스 버전 컨트롤

## 설치

```
pip install Flask-Migrate
```

## Migrate 설정

app.py

```
from flask_migrate import Migrate

migrate = Migrate(app, db)
```

### 초기 Migration 생성

데이터베이스 마이그레이션을 사용하기 위해 초기 마이그레이션 파일 생성이 필요

```
flask db init
```

## flask db Migrate

- github commit과 비슷

```
flask db migrate
flask db migrate -m "Your migration message"
```

## flask db upgrade

- github push와 비슷

```
flask db upgrade
```

# Flask Authentication

## 1. Session

- Session 웹-애플리케이션이 사용자의 상태를 유지하기 위해 주로 사용됨. 서버 측에 사용자 정보를 기록하고, 로그아웃하면 그 상태를 제거함.
- 왜 필요한가?
  - HTTP는 stateless 프로토콜이기 때문에, session을 통하여 서버에 저장.

### 보안상의 문제

- 브라우저는 세션 ID를 쿠키에 저장하므로, 쿠키가 해킹될 가능성이 있음.
- SECRET_KEY의 유출 위험
  - SECRET_KEY > 암호화 하는 키.
- 서버의 리소스를 많이 잡아먹음.

### 세션 인증의 동작 방식

- 로그인 > 세션 ID > 상태 유지 > 로그아웃

1. 로그인: 사용자가 로그인 폼을 제출하면, 서버는 이를 검증하고 세션에 사용자 인증 정보를 저장.

2. 세션ID: 저장된 인증 정보를 서버 내의 고유한 세션 ID 생성 및 브라우저에 쿠키 형태로
   전송. 이후 모든 요청에서 세션ID를 서버에 전송.

3. 상태 유지: 서버는 받은 세션 ID를 사용하여 사용자의 인증 상태와 관련 데이터를 조회. 로그인 상태 확인, 해당 사용자에게 적절한 응답 제공.

4. 로그아웃: 사용자 로그아웃 시, 서버는 해당 사용자의 세션을 제거하고 세션ID를 무효화.

## Flask 기본 세션 모듈에서 제공하는 함수

**`session`** 객체는 사용자의 브라우저에 저장된 쿠키와 연결되어 있으며, 사전(dictionary) 형태로 작동하여 세션 데이터를 저장하고 접근합니다.

**(1) `session`에 데이터 저장하기**

**데이터 추가**: **`session`** 객체에 새로운 키와 값을 추가할 수 있습니다.

```python
session['username'] = 'john'
```

**(2)`session`에서 데이터 가져오기**

**데이터 읽기**: **`session`** 객체에서 키를 사용하여 데이터를 읽을 수 있습니다.

```python
username = session['username']
```

**`get` 메소드 사용**: 키가 존재하지 않을 경우 **`None`**을 반환하도록 **`get`** 메소드를 사용할 수 있습니다.

```python
username = session.get('username')
```

**(3) `session`에서 데이터 제거하기**

**데이터 삭제**: **`pop`** 메소드를 사용하여 특정 키와 그에 대응하는 값을 세션에서 제거할 수 있습니다.

```python
session.pop('username', None)
```

**세션 클리어**: **`clear`** 메소드를 사용하여 세션의 모든 데이터를 제거할 수 있습니다.

```python
session.clear()
```

- 특정 사용자와 관련된 모든 세션 데이터를 서버 측에서 삭제하는 데 사용
  주로 사용자가 로그아웃할 때, 사용자와 관련된 모든 세션 데이터를 삭제함.

**(4) 세션 유지 기간 설정**

**`permanent`** 속성을 **`True`**로 설정하여 세션의 유지 기간을 **`PERMANENT_SESSION_LIFETIME`** 설정값에 따라 조정 가능

**app.py**

```python
from datetime import timedelta

app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)  # 예: 7일
```

**routes/user.py**

```python
@app.route('/login', methods=['POST'])
def login():
    session['username'] = 'your_username'
    session.permanent = True  # 세션 유지 기간을 활성화
    return redirect(url_for('secret'))
```

## 2. HTTP 기본 인증

### Flask HTTP-Auth

라이브러리 설치

```
pip insatll Flask-HTTPAuth
```

- `@**auth.verify_password**` (사용자 인증)
  사용자 이름과 비밀번호가 유효한지 확인하는 함수를 정의합니다. 여기서는 간단한 사전 **`users`**를 사용하여 사용자 이름과 비밀번호를 확인합니다. 실전 환경에서는 데이터베이스 또는 다른 안전한 저장소를 사용해야합니다.
- **`@auth.login_required`** (라우트 보호)
  인증된 사용자만 해당 라우트로 접근할 수 있도록하는 목적. 사용자 인증을 요구.
- **`@auth.error_handler`** (오류 핸들링)
  인증에 실패했을 때의 동작을 정의
  위 코드에서는 403 상태 코드와 함께 오류 메시지를 반환

## 3. Flask-Login

라이브러리 설치

```
pip install flask-login
```

### 필요한 라이브러리 불러오기

routes.py

```
from flask import render_template, request, url_for, redirect, flash
from models import User, users
from flask_login import login_user, logout_user, login_required
```

app.py

```
from flask import Flask
from flask_login import LoginManager
# LoginManager 클래스를 가져오는 코드 (로그인 상태 관리, 세션 저장, 로그인 처리 담당)
from models import User
from routes import configure_route
```

models.py

```
from flask_login import UserMixin # 기본 사용자 기능을 자동으로 구현해주는 믹스인 클래스

users = {'admin' : {'password': 'qwe123'}} # 유저 정보 DB

class User(UserMixin):  #  User 클래스 정의
    def __init__(self, username):
        self.id = username

    @staticmethod # 객체 없이 호출 가능
    def get(user_id): # 세션에서 가져온 user_id로 사용자 객체를 복원하는 용도
        if user_id in users:
            return User(user_id)

```

### 각 파일 코드 작성

#### 파일 디렉토리

```
├─app.py
├─models.py
├─routes.py
└─templates.py
    ├─index.html
    └─login.html
```

index.html

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <a href="/login">Login</a>
    <a href="/logout">Logout</a>
    <a href="/protected">Protected</a>
</body>
</html>
```

login.html

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form method="post">
        Username: <input type="text" name="username" /><br/>
        Password: <input type="password" name="password" /><br/>
        <input type="submit" value="login" />
    </form>
</body>
</html>
```

routes.py

```
from flask import render_template, request, url_for, redirect, flash
from models import User, users
from flask_login import login_user, logout_user, login_required #


def configure_route(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/login', methods=['GET','POST'])
    def login():
        if request.method == 'POST': # FE 단에서 BE로 폼 전송
            username = request.form['username']
            password = request.form['password']

            user = User.get(username) # 유저 네임 받기

            if user and users[username]['password'] == password:
                login_user(user) # 'login_user' -> flask login Library

                return redirect(url_for('index'))
            else:
                flash('Invalid username or password')

        return render_template('/protected')

    @app.route('/logout') # 로그아웃 설정
    def logout():
        logout_user()
        return redirect('/') # 로그아웃 시, 홈페이지로 리디렉션

    @app.route('/protected') # 로그인 성공 페이지
    @login_required
    def protected():
        return "<h1>Protected Area</h1> <a href='/logout'>Logout</a>"

```

app.py

```
from flask import Flask
from flask_login import LoginManager # LoginManager 클래스를 가져오는 코드 (로그인 상태 관리, 세션 저장, 로그인 처리 담당)
from models import User
from routes import configure_route

app = Flask(__name__)
app.secret_key = 'flask-secret-key' # 암호화 설정

login_manager = LoginManager() # 함수 불러오기
login_manager.init_app(app) # init_app을 통해 초기화
login_manager.login_view = 'login'  # login view를 결정한다. 그게 뭔데? 로그인을 했을 때,
                                    # 자동으로 이동할 로그인 페이지의 라우트 이름을 지정

@login_manager.user_loader
def load_user(user_id): # user_id -> 세션에서 가져옴
    return User.get(user_id)

configure_route(app)

if __name__ == "__main__":
    app.run(debug=True)
```

models.py

```
from flask_login import UserMixin # 기본 사용자 기능을 자동으로 구현해주는 믹스인 클래스

users = {'admin' : {'password': 'qwe123'}} # 유저 정보 DB

class User(UserMixin):  #  User 클래스 정의
    def __init__(self, username):
        self.id = username

    @staticmethod # 객체 없이 호출 가능
    def get(user_id): # 세션에서 가져온 user_id로 사용자 객체를 복원하는 용도
        if user_id in users:
            return User(user_id)

```

## 4. JWT-Extended

- JSON Web Token(JWT)을 쉽게 다룰 수 있도록 해주는 확장 라이브러리
  - JWT: 사용자 인증 및 권한 부여에서 널리 사용되는 방식으로 서버와 클라이언트 간의 안전한 정보전달

설치

```
pip install Flask-JWT-Extended
```

## **요약**

Flask JWT-Extended를 사용하여 간단한 JWT 기반 인증 시스템을 구축

1. **`app.py`**에서 Flask 애플리케이션을 설정하고 JWT 인증 라우트를 정의합니다.
2. **`models/user.py`**에서 사용자 모델을 정의합니다.
3. **`jwt_utils.py`**에서 JWT 설정과 인증 관련 유틸리티 함수를 정의합니다.

| Method   | Endpoint          | Description                                           |
| -------- | ----------------- | ----------------------------------------------------- |
| `POST`   | `/register`       | Create user accounts given an `email` and `password`. |
| `POST`   | `/login`          | Get a JWT given an `email` and `password`.            |
| 🔒`POST` | `/logout`         | Revoke a JWT.                                         |
| 🔒`POST` | `/refresh`        | Get a fresh JWT given a refresh JWT.                  |
| `GET`    | `/user/{user_id}` | (dev-only) Get info about a user given their ID.      |
| `DELETE` | `/user/{user_id}` | (dev-only) Delete a user given their ID.              |

## JWTManager에서 사용할 수 있는 주요 데코레이터

(1) **`@jwt_required()`**:

```python
from flask_jwt_extended import jwt_required

@jwt_required()
def protected_route():
    # 이 라우트는 JWT가 필요합니다.
    # JWT가 유효하면 실행됩니다.
```

이 데코레이터는 해당 엔드포인트에 접근하려면 JWT가 필요하다는 것을 나타냅니다. 클라이언트는 유효한 JWT를 제공해야만 해당 라우트에 접근할 수 있습니다.

(2) **`@jwt_optional()`**:

```python
from flask_jwt_extended import jwt_optional

@jwt_optional()
def optional_route():
    # 이 라우트는 JWT가 선택적입니다.
    # JWT가 제공되면 유효성을 확인하고, 제공되지 않으면 계속 진행합니다.
```

이 데코레이터는 해당 엔드포인트에 클라이언트가 JWT를 제공할 수 있지만, 필수적이지 않다는 것을 나타냅니다. 클라이언트가 JWT를 제공하면 이를 확인하고 유효성을 검사하며, 제공되지 않으면 계속 진행합니다.

(3)**`@fresh_jwt_required()`**:

```python
from flask_jwt_extended import fresh_jwt_required

@fresh_jwt_required()
def fresh_route():
    # 이 라우트는 fresh한 JWT가 필요합니다.
    # JWT가 fresh하지 않으면 해당 라우트에 접근할 수 없습니다.
```

이 데코레이터는 해당 엔드포인트에 접근하려면 fresh한 JWT가 필요하다는 것을 나타냅니다. JWT가 fresh하지 않으면 해당 라우트에 접근할 수 없습니다. 또한 **`@jwt_required(optional=True)`**, **`@jwt_required(fresh=True, optional=True)`** 등의 옵션을 사용하여 더 세부적인 제어가 가능합니다.

(4) **`@jwt_refresh_token_required()`**:

```python
from flask_jwt_extended import jwt_refresh_token_required

@jwt_refresh_token_required()
def refresh_route():
    # 이 라우트는 refresh token이 필요합니다.
    # refresh token이 유효하면 해당 라우트에 접근할 수 있습니다.
```

이 데코레이터는 해당 엔드포인트에 접근하려면 refresh token이 필요하다는 것을 나타냅니다. refresh token이 유효하면 해당 라우트에 접근할 수 있습니다.

### BLOCKLIST

- 로그인을 관리하는 함수 그니까, 이 토큰을 여걸로 관리해서 있다 없다를 알려줌

### 코드

디렉토리

```
├─app.py
├─blocklsist.py
├─jwt_utils.py
├─models
│   └─user.py
├─routes
│   └─user.py
└─templates
    ├─index.html
    ├─login.html
    └─protect.html
```

app.py

```
from flask import Flask, render_template
from routes.user import user_bp
from jwt_utils import configure_jwt  # JWT 설정 함수를 임포트합니다.

app = Flask(__name__)
configure_jwt(app)  # JWT 관련 추가 설정을 적용합니다.

app.register_blueprint(user_bp, url_prefix='/user')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
```

blocklsist.py

```
# 블록리스트 관리 파일

BLOCKLIST = set()

def add_to_blocklist(jti):
    BLOCKLIST.add(jti)

def remove_from_blocklist(jti):
    BLOCKLIST.discard(jti)
```

jwt_utils.py

```
from flask_jwt_extended import JWTManager
from blocklist import BLOCKLIST
from flask import jsonify

jwt = JWTManager()

def configure_jwt(app):
    app.config["JWT_SECRET_KEY"] = "flask-secret-key"

    # 토큰 만료시간 설정
    freshness_in_minutes = 1
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = freshness_in_minutes * 60 # 1 hour
    jwt.init_app(app)

    # 추가적인 정보를 토큰에 넣기
    @jwt.additional_claims_loader #데코레이터
    def add_claim_to_jwt(identity):
        if identity == 1:
            return {"is_admin": True}
        return {"is_admin": False}

    # 토큰이 블록리스트 내에 있는지 확인
    @jwt.token_in_blocklist_loader
    def check_if_token_in_blocklist(jwt_header, jwt_payload):
        return jwt_payload["jti"] in BLOCKLIST

    # 만료된 토큰이 사용되었을 때 실행되는 함수
    @jwt.expired_token_loader
    def expirede_token_callback(jwt_header, jwt_payload):
        return jsonify({"msg": "Token exprired", "error": "token_expired"}), 401

    # 유효하지 않은 토큰이 사용되었을 때
    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return (
            jsonify (
                {"message": "invalid token"},
            ), 401
        )

    # 해당 토큰으로 접근 권한이 없는 경우
    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return (
            jsonify(
                {
                    'description': "Access token required",
                    "error": "access_token_required"
                }
            ), 401
        )

    # fresh한 토큰이 필요한데 fresh하지 않은 토큰이 사용되었을 때 실행되는 함수를 정의
    # fresh 토큰이 필요하다는 메세지 전달 및 토큰 만료시간 조절
    @jwt.needs_fresh_token_loader
    def token_not_fresh_callback(jwt_header, jwt_payload):
        return (
            jsonify(
                {"description": "Token is not fresh.",
                "error": "fresh token required"
                }
            ),
            401
        )

    # 토큰이 폐기되었을 때 실행되는 함수
    @jwt.revoked_token_loader
    def revoked_token_calllback(jwt_header, jwt_payload):
        return (
            jsonify(
                {"description": "Token has been revoked", "error": "token_revoked"}
            ),
            401
        )
```

models/user.py

```
class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.username = password
```

routes/user.py

```
from flask import Blueprint, jsonify, request, render_template
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from models.user import User

user_bp = Blueprint('user', __name__)

# 임시 사용자 데이터
users = {
    'user1': User('1', 'user1', 'pw123'),
    'user2': User('2', 'user2', 'pw123')
}

@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.json.get('username', None)
        password = request.json.get('password', None)

        user = users.get(username)
        if user and user.password == password:
            access_token = create_access_token(identity=username)
            refresh_token = create_refresh_token(identity=username)
            return jsonify(access_token=access_token, refresh_token=refresh_token)
        else:
            return jsonify({"msg": "Bad username or password"}), 401
    else:
        return render_template('login.html')


@user_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

@user_bp.route('/protected_page')
def protected_page():
    return render_template('protected.html')

from flask_jwt_extended import get_jwt
from blocklist import add_to_blocklist  # 블랙리스트 관리 모듈 임포트
@user_bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    jti = get_jwt()["jti"]
    add_to_blocklist(jti)  # jti를 블랙리스트에 추가
    return jsonify({"msg": "Successfully logged out"}), 200
```

templates/index.html

```
<!DOCTYPE html>
<html>
  <head>
    <title>Home Page</title>
  </head>
  <body>
    <h1>Welcome to the Home Page</h1>
    <a href="/user/login">Login</a> | <a href="/user/logout">Logout</a>
    <a href="/user/protected">Protected Page</a>
  </body>
</html>
```

templates/login.html

```
<!DOCTYPE html>
<html>
  <head>
    <title>Login</title>
    <script>
      function handleLogin(event) {
        event.preventDefault(); // 폼의 기본 제출 동작을 방지

        // 폼 데이터를 JSON으로 변환
        var username = document.getElementById("username").value;
        var password = document.getElementById("password").value;
        var data = { username: username, password: password };

        // fetch를 사용하여 서버에 POST 요청 보내기
        fetch("/user/login", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(data),
        })
          .then((response) => response.json())
          .then((data) => {
            console.log("Success:", data);
            // 로그인 성공 후 'protected' 페이지로 리다이렉트
            localStorage.setItem("access_token", data.access_token);
            localStorage.setItem("refresh_token", data.refresh_token);
            window.location.href = "/user/protected_page";
          })
          .catch((error) => {
            console.error("Error:", error);
          });
      }
    </script>
  </head>
  <body>
    <h1>Login</h1>
    <form onsubmit="handleLogin(event)">
      Username: <input type="text" id="username" name="username" /><br />
      Password: <input type="password" id="password" name="password" /><br />
      <input type="submit" value="Login" />
    </form>
  </body>
</html>
```

templates/protect.html

```
<!DOCTYPE html>
<html>
  <head>
    <title>Protected Page</title>
    <script>
      document.addEventListener("DOMContentLoaded", function () {
        const token = localStorage.getItem("access_token");
        console.log("token", token);
        if (token) {
          fetch("/user/protected", {
            headers: {
              Authorization: `Bearer ${token}`, // 보호되는 페이지에 써야함 Bearer
            },
          })
            .then((response) => {
              if (response.ok) {
                return response.json();
              } else {
                throw new Error("Access Denied");
              }
            })
            .then((data) => {
              document.getElementById("content").innerHTML =
                "Welcome, " + data.logged_in_as;
            })
            .catch((error) => {
              document.getElementById("content").innerHTML = "Access Denied";
              console.error("Error:", error);
            });
        } else {
          document.getElementById("content").innerHTML =
            "No token found, please login.";
        }
      });
    </script>
  </head>
  <body>
    <h1>This is a Protected Page</h1>
    <div id="content">
      <p>Loading...</p>
    </div>
    <button onclick="logout()">Logout</button>
  </body>
  <script>
    // 로그아웃 함수
    function logout() {
      // 로컬 스토리지에서 JWT 토큰 제거
      localStorage.removeItem("access_token");
      localStorage.removeItem("refresh_token");

      // 로그인 페이지 또는 홈페이지로 리다이렉트
      window.location.href = "/";
    }
  </script>
</html>
```

# Flask MiniProject

- User Management Web
- Instargram RESTAPI
- TodoList

## User-ManagementWeb

- Flask N Jinja

Goals

- 사용자 목록 표시, 추가, 삭제 기능
- Flask 라우트 및 Jinja 템플릿 상ㅇ
- 사용자 입력 처리 및 데이터를 서버에서 관리

Request

- 라우트 설정
  - 사용자 목록을 표시하는 라우트를 포함하여, 사용자 추가(`/add`), 수정(`/edit/<username>`), 삭제(`/delete/<username>` )기능을 수행하는 라우트 설정
- 템플릿 설정
  - 사용자 목록, 추가, 삭제, 수정 기능 HTML 작성
  - 사용자 추가 및 수정을 위한 폼 기능
  - 각 사용자에 대한 수정 및 삭제 옵션 제공
- 폼 데이터 처리 및 서버 로직 구현
  - 사용자 추가 및 수정에 대한 폼 데이터를 처리하는 백엔드 로직 구현
  - 유효성 검증 및 피드백 제공
- 애플리케이션 실행 및 테스트

### 파일 구조

```
├─app.py
└─templates
    ├─index.html
    ├─add_user.html
    └─edit_user.html
```

app.py

```
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 임시 사용자 데이터
users = [
    {"username": "traveler", "name": "Alex"},
    {"username": "photographer", "name": "Sam"},
    {"username": "gourmet", "name": "Chris"}
]

@app.route('/')
def index():
    return render_template('index.html', users=users)

# 사용자 추가, 수정, 삭제 라우트 및 함수 작성...

if __name__ == '__main__':
    app.run(debug=True)
```

templates/index.html

```
<!DOCTYPE html>
<html>
<head>
    <title>User Management</title>
</head>
<body>
    <h1>User List</h1>
    <ul>
    {% for user in users %}
        <li>{{ user.name }} ({{ user.username }})
            <a href="/edit/{{ user.username }}">Edit</a>
            <a href="/delete/{{ user.username }}">Delete</a>
        </li>
    {% endfor %}
    </ul>
    <a href="/add">Add User</a>
</body>
</html>
```

templates/add_user.html

```
<!DOCTYPE html>
<html>
<head>
    <title>Add User</title>
</head>
<body>
    <h1>Add User</h1>
    <form method="post">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name">
        <input type="submit" value="Add">
    </form>
    <a href="{{ url_for('index') }}">Back</a>
</body>
</html>
```

templates/edit_user.html

```
<!DOCTYPE html>
<html>
<head>
    <title>Edit User</title>
</head>
<body>
    <h1>Edit User</h1>
    <form method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" value="{{ user.name }}">
        <input type="submit" value="Update">
    </form>
    <a href="{{ url_for('index') }}">Back</a>
</body>
</html>
```

# 기타

정적 웹사이트
클라이언트 <=> 웹 서버

동적 웹사이트
클라이언트 <=>
웹 서버(NGiNX) <=>
Gateway Interface(WSGI) <=>
웹 어플리케이션 서버(Flask, Django) <=(ORM)=>
Database

# 미주

- oz코딩스쿨
- 한 권으로 정리하는 파이썬 백엔드
- 플라스크 공식문서 https://flask-docs-kr.readthedocs.io/ko/latest/
- 본인 벨로그: https://kkjjww1102.tistory.com/5
- smorest velog: https://velog.io/@legendofjiwon/flask-smorest
- smorest doc: https://flask-smorest.readthedocs.io/en/latest/
