from flask import Flask, render_template
from flask_httpauth import HTTPBasicAuth # pup install flask-httpauth

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    'admin' : 'secret'
}

@auth.verify_password
def verify_password(username, password): # 패스워드 인증.
    if username in users and users[username] == password:
        return username 

@app.route('/') # 홈 화면
def index():
    return render_template('index.html')

@app.route('/protected') 
@auth.login_required
def protected():
    return render_template('secret.html')

if __name__ == "__main__": # 
    app.run(debug=True)