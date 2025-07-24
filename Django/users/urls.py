from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
	TokenVerifyView
)

urlpatterns = [
    path("", views.Users.as_view()),
    path("myinfo/", views.MyInfo.as_view()),

    # Token Authentications
    path("getToken", obtain_auth_token),
    path("login/", views.Login.as_view()),
    path("logout/", views.Logout.as_view()),
    
    # JWT
    path("login/jwt", views.JWTLogin.as_view()),
    path("login/jwt/userinfo", views.UserDetailView.as_view()),

    # Simple JWT
    path("login/simpleJWT", TokenObtainPairView.as_view()),
    path("login/simpleJWT/refresh", TokenRefreshView.as_view()),
    path("login/simpleJWT/verify", TokenVerifyView.as_view()),
]
