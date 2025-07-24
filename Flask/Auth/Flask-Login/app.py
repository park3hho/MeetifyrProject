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