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