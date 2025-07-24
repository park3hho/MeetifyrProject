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