from flask import Flask
from flask_restful import Resource, Api
import os

import api

PORT = os.environ['PORT']
try:
    PORT=int(PORT)
except:
    PORT = 5000

app = Flask(__name__)
flaskApi = Api(app)


class Usage(Resource):
    def get(self):
        return "Check a number is prime."

class PrimeList(Resource):
    def get(self, start=1, end=20):
        return api.prime_list(start=start, end=start+end)

class IsPrime(Resource):
    def get(self, num):
        return api.prime_text(num)

flaskApi.add_resource(Usage, '/')
flaskApi.add_resource(IsPrime, '/<int:num>')
flaskApi.add_resource(PrimeList, '/list', '/list/<int:start>', '/list/<int:start>/<int:end>')

if __name__ == '__main__':
    print(f'Start host using port: {PORT}')
    app.run(debug=False, host='0.0.0.0', port=PORT)