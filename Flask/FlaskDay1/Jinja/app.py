from flask import Flask, render_template
app = Flask(__name__)

# 기본 경로 설정
@app.route('/')
def index():
    data = {
        'title': 'jinja2',
        'user': 'John Doe',
        'is_admin': True,
        'items': ['apple', 'banana', 'cherry'],
    }

    # render_template는 Flask에서 제공하는 함수로, HTML 파일을 렌더링하고 데이터를 전달
    # **data는 data 딕셔너리의 키-값 쌍을 개별 인자로 전달
    return render_template('index.html', **data)

__name__ = '__main__'
# 실시간 변화를 확인하기 위해 debug 모드로 실행
app.run(debug=True)