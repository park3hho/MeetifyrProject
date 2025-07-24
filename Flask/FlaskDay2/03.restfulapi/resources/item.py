from flask import request
from flask_restful import Resource

items = [] # DB

class Item(Resource):
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item
        return {"msg": "Item not found"}, 40


    def post(self,name):
        for item in items:
            if item['name'] == name:
                return {"msg": "Item already exists"}, 400

        data = request.get_json()
        new_item = {
            'name': name,
            'price': data['price']  
        }
        items.append(new_item)

        return new_item, 201

    #update item
    def put(self, name):
        data = request.get_json()
        for item in items:
            if item['name'] == name:
                item['price'] = data['price']
                return item, 200

        #if new item has no data, create a item
        new_item = {
            'name': name,
            'price': data['price']
        }
        items.append(new_item)
        return new_item, 201

    #delete item
    def delete(self, name):
        global items
        items = [item for item in items if item['name'] != name]
        
        return {"msg": "Item deleted"}, 200