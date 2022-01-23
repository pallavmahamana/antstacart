from flask import Flask, request
from flask_restful import Resource, Api
from datetime import datetime
from util import InvoiceGenerator

app = Flask(__name__)
api = Api(app)


class GenerateInvoice(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        order = InvoiceGenerator(json_data)
        order.calculate_order()
        return {"commodities":order._commodities,
                "total_order":{
                    "datetime": str(datetime.now()),
                    "total_amount_without_discount": order._total_amount,
                    "total_tax_amount": order._total_tax,
                    "discount_applied": order.apply_discount(),
                    "total_amount_with_discount": order._total_amount_with_discount

                }}





api.add_resource(GenerateInvoice,'/invoice')


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=4455,debug=True)