from flask.views import MethodView 
# methodsview가 뭐지 아하, 클래시 기반 뷰이며, GPPD 하기 위한 거군 "from flask import Flask 대용"
from flask_smorest import Blueprint, abort # smorest에서 blueprint, abort 추출
from schema import BookSchema #schema.py 추출

book_blp = Blueprint('books', 'books', url_prefix='/books') # 블루프린트 생성, 'books'는 이름, 'books'는 식별자, url_prefix는 '/books'

books = [] #DB 역할

#클래스 생성
@book_blp.route('/')
class BookList(MethodView):
    # 책 목록 부르기
    @book_blp.response(200, BookSchema(many=True)) # 여러 개의 책을 반환
    def get(self):
        return books

    @book_blp.arguments(BookSchema) # 책 생성 시 필요한 데이터 검증
    @book_blp.response(201, BookSchema) # 책 생성 후 반환
    def post(self, new_data):  # 책 생성
        new_data['id'] = len(books) + 1 # ID 하드코딩
        books.append(new_data)
        return new_data

@book_blp.route('/<int:book_id>') # 타입힌팅
class Book(MethodView): 
    # 책 조희하기 
    @book_blp.response(200, BookSchema)
    def get(self, book_id):
        book = next((book for book in books if book['id'] == book_id), None)

        if book is None:
            abort(404, message="Book not found.") # 없으면 404

        return book
    # 책 수정하기
    @book_blp.arguments(BookSchema)
    @book_blp.response(200, BookSchema)
    def put(self, new_data, book_id):
        book = next((book for book in books if book['id'] == book_id), None)

        if book is None:
            abort(404, message="Book not found.")
        book.update(new_data)

        return book

    @book_blp.response(204)

    def delete(self, book_id):
        global books # 전역변수로 books를 사용하기 위해 global 선언
        book = next((book for book in books if book['id'] == book_id), None)\
        
        if book is None: 
            abort(404, message="Book not found.")
        books = [book for book in books if book['id'] != book_id] # books에서 해당 ID의 책을 제거

        return ''