from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)


class GenerateInvoice(Resource):
    def post(self):
        json_data = request.get_json()
        print(json_data)
        return "OK"




api.add_resource(GenerateInvoice,'/invoice')


if __name__ == '__main__':
    app.run(host='127.0.0.9',port=4455,debug=True)