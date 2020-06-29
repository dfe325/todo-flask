from flask import Flask, request, jsonify
from models import Schema
from service import ToDoService
import json

app = Flask(__name__)

@app.after_request
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] =  "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
    response.headers['Access-Control-Allow-Methods']=  "POST, GET, PUT, DELETE, OPTIONS"
    return response

@app.route("/")
def hello():
    return "Hello world!"

@app.route("/todo", methods=["POST"])
def create_todo():
    return jsonify(ToDoService().create(request.get_json()))

@app.route("/todo", methods=["GET"])
def list_todo():
    return jsonify(ToDoService().list())

if __name__ == "__main__":
    Schema()
    app.run(debug=True)

