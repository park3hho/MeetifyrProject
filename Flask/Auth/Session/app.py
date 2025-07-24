from flask import Flask, render_template, request, redirect, url_for, session, flash
# render_template HTML 렌더링
# request 클라이언트 요청 받기
# url_for url 경로 동적 생성
# session 서버에 저장 안하고 쿠키를 통해 관리
# flash 사용자에게 잠깐 보여줄 메세지

app = Flask(__name__) # __name__ > 현재 모듈의 이름이 저장. Flask() > 앱의 위치를 알려줌.

app.secret_key = 'flask-secret-key' # 실제로 배포시 .env or yaml로 사용.

# admin user
users = {
    'john':'pw123',
    'leo':"pw344"
}

@app.route('/') # 메인 페이지
def index():
    return render_template("login.html") # 로그인 페이지로 유도

@app.route('/login', methods=['POST']) # 로그인 페이지
def login(): 
    username = request.form['username'] # 폼 제출 시 'username' 가져오기
    password = request.form['password'] # 폼 제출 시 'password' 가져오기

    if username in users and users[username] == password: # 패스워드 같으면, 세션에 저장
        session['username'] = username # 세션에 유저 이름 저장
        return redirect('/secret') # secret.html로 유도
    
    else: 
        flash('invalid username or password')
        return redirect('/') # 틀리면 홈으로 유도
    
# 세션 작업. 세션이 있으면 secret.html 부르기
@app.route('/secret')
def secret():
    if 'username' in session: # 세션에 유저 이름 있으면  secret.html 로 유도
        return render_template('secret.html')
    else: 
        return redirect('/')
    
# 로그아웃
app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)