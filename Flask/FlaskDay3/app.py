from flask import Flask
from flask_smorest import Api
from db import db
from models import User, Board
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() # db intitialized here
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:As583346@localhost/oz' #MySQL 연결
#데이터 베이스 접근 (위의 한줄로)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #추적 기능 비활성화
db.init_app(app)  # db 객체를 Flask 앱에 연결, db객체는 중복 사용하므로 모듈화

migrate = Migrate(app, db)

#blueprint 설정
app.config['API_TITLE'] = 'My API'
app.config['API_VERSION'] = 'v1'
app.config['OPENAPI_VERSION'] = '3.1.3'     
app.config['OPENAPI_URL_PREFIX'] = '/'  # OpenAPI URL 접두사 설정
app.config['OPENAPI_SWAGGER_UI_PATH'] = '/swagger-ui'  # Swagger UI 경로 설정
app.config['OPENAPI_SWAGGER_UI_URL'] = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/'  # Swagger UI 리소스 URL

api = Api(app)  # Api 객체 생성

from routes.board import board_blp # /routes/board 불러오기
from routes.user import user_blp # /routes/user 불러오기

api.register_blueprint(board_blp) # blueprint등록
api.register_blueprint(user_blp) # blueprint 등록

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
