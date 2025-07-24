from flask_login import UserMixin # 기본 사용자 기능을 자동으로 구현해주는 믹스인 클래스

users = {'admin' : {'password': 'qwe123'}} # 유저 정보 DB

class User(UserMixin):  #  User 클래스 정의
    def __init__(self, username): 
        self.id = username

    @staticmethod # 객체 없이 호출 가능
    def get(user_id): # 세션에서 가져온 user_id로 사용자 객체를 복원하는 용도
        if user_id in users:
            return User(user_id)
