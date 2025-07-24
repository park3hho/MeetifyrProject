from flask import render_template, request, url_for, redirect, flash
from models import User, users
from flask_login import login_user, logout_user, login_required #


def configure_route(app):
    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/login', methods=['GET','POST'])
    def login():
        if request.method == 'POST': # FE 단에서 BE로 폼 전송
            username = request.form['username']
            password = request.form['password']

            user = User.get(username) # 유저 네임 받기

            if user and users[username]['password'] == password:
                login_user(user) # 'login_user' -> flask login Library

                return redirect(url_for('index'))
            else:
                flash('Invalid username or password')
        
        return render_template('/protected')
    
    @app.route('/logout') # 로그아웃 설정
    def logout():
        logout_user()
        return redirect('/') # 로그아웃 시, 홈페이지로 리디렉션

    @app.route('/protected') # 로그인 성공 페이지
    @login_required
    def protected():
        return "<h1>Protected Area</h1> <a href='/logout'>Logout</a>"
    