import jwt
from rest_framework.authentication import BaseAuthentication
from django.conf import settings
from users.models import User

# JWT Decoding and Authentication
class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.headers.get("jwt-auth") # Assuming the token is passed in the header as "jwt-auth"

        if not token:
            return None
        
        decodedToken = jwt.decode(token, 
                    settings.SECRET,
                    algorithms=["HS256"]) # 토큰 디코딩. 
        
        user_id = decodedToken.get("id") # 디코드 된 토큰에서 아이디 값 가져오기 
        user = User.objects.get(id=user_id) # 

        return (user, None) # 토큰은 이미 보냈으니 더 보낼 필요 없다.  