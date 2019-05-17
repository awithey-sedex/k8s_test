from flask import Flask
from flask_restful import Resource, Api

import service

app = Flask(__name__)
api = Api(app)


class Usage(Resource):
    def get(self):
        return "Check a number is prime."

class IsPrime(Resource):
    def get(self, num):
        return service.is_prime_number(num)

api.add_resource(IsPrime, '/<int:num>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')