from flask import Flask, request, jsonify
from pymongo import MongoClient
import json
import os

app = Flask(__name__)
mongo_url = os.environ.get("MONGO_URL", "mongodb://127.0.0.1:27017/")
client = MongoClient(mongo_url)
db = client['mydatabase']
collection = db['mycollection']

@app.route('/', methods=['GET'])
def get_objects():
    objects = collection.find_one()
    del objects['_id']
    return jsonify(objects)

@app.route('/', methods=['PUT'])
def add_object():
    data = request.form
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    new_object = data.to_dict()
    for i in new_object.keys():
        data_dict = json.loads(i)
        collection.insert_one(data_dict)
    
    return jsonify({})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)