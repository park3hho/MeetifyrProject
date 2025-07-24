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