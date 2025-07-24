# 백엔드를 위한 DJANG REST FRAMEWORK with 파이썬
- Python
- DJANGO
- REATCT.JS
- HEROKU
---
# 프로젝트 시작하기

1. 프로젝트 시작
2. 프로젝트 설정 마무리
### 1. 프로젝트 시작
```
python --version
python -m venv myvenv
source myvenv/bin/activate
pip insatll django~=3.2.10
django-admin startproject startproject myweb .
python manage.py startapp photo 
python manage.py runserver
```

### 2. 프로젝트 설정 마무리
myweb/setting.py
```
INSTALLED_APPS = [
    ...
    'photo' # 추가 
]

TIME_ZONE = 'Asia/Seoul' # 1. 시간대 한국으로 설정
```

### admin Page 들어가기
```
python manage.py migrate # 1. migrate 오류 해결
python manage.py createsuperuser # 2. 어드민 계정 생성 
```

# Model View Template

- 0. model
- 1. adminPage
- 2. temaplates
- 3. View
- 4. URL  

### 0. model 작성 및 migration
```
# model 작성 완료
python manage.py makemigrations
python maange.py migrate
```

### 1. adminPage 적용 
```
from .models import Photo

admin.site.register(Photo)
```

### 2. Templates 생성
```
/photo/templates/photo.html  # 1. Templates 생성 및 html 코드 작성
# 2. HTML 코드 작성
```

### 3. View 작성
```

```


### 4. URL 작성
