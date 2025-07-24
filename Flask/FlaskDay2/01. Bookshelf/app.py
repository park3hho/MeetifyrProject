from flask import Flask # Flask 애플리케이션 생성
from flask_smorest import Api # API
from api import book_blp # 책 블루프린트

app = Flask(__name__) # Flask 애플리케이션 인스턴스 생성

#OpenAPI 설정정
app.config['API_TITLE'] = 'Book API' # API 제목
app.config['API_VERSION'] = 'v1' # API 버전
app.config['OPENAPI_VERSION'] = '3.0.2' # OpenAPI 버전
app.config["OPENAPI_URL_PREFIX"] = "/" # OpenAPI URL 접두사
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui" # Swagger UI 경로, 예쁘게 보이게 함
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/" 
# Swagger UI URL, CDN에서 가져옴
api = Api(app) # Api 객체 생성
api.register_blueprint(book_blp) # 블루프린트 등록

# Flask 애플리케이션 실행
if __name__ == '__main__':
    app.run(debug=True)