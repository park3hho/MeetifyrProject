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