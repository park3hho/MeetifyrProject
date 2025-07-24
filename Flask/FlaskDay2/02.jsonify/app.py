from flask import Flask, jsonify
from flask import request

app = Flask(__name__)
# GET
@app.route('/api/v1/feeds', methods=['GET'])
def get_all_feeds():
    data={'result': 'success', 'feeds': ['feed1', 'feed2', 'feed3']}
    return jsonify(data) 

# POST
# (1) Create a new feed
@app.route('/api/v1/feeds', methods=['POST'])
def create_feed():
    name = request.form['name']

    print(name)

    return jsonify({'result': 'success'})

data = [{"items": [{"name": "item1", "price": "item2"}]}]

@app.get('/api/v1/datas')
def create_data():
    return {"data": data}   

@app.post('/api/v1/datas')
def create_data_post():
    request_data = request.get_json()
    new_data = {'items': request_data.get("items", [])}
    data.append(request_data)
    return jsonify(new_data), 201