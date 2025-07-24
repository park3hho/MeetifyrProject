from flask import Flask
from flask_restful import Api
from resources.item import Item

app = Flask(__name__)
api = Api(app)

if __name__ == '__main__':
    app.run(debug=True)

api.add_resource(Item, '/item/<string:name>') # add default route