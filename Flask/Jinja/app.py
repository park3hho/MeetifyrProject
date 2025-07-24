from flask import Flask, render_template
app = Flask(__name__)

# 기본 라우팅
@app.route('/') 
def index():
    data = {
        'title': 'jinja2',
        'user': 'John Doe',
        'is_admin': True,
        'items': ['apple', 'banana', 'cherry'],
    }
    # (1) Render html file, (2) 넘겨줄 html data
    return render_template('index.html', **data)

__name__ = '__main__'
app.run(debug=True)