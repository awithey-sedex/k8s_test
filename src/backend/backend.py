from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)


class Usage(Resource):
    def get(self):
        return "Check a number is prime."

class IsPrime(Resource):
    def get(self, num):
        if num >= 2:
            for y in range(2,num):
                if not ( num % y ):
                    return False
        else:
            return False
        return True

api.add_resource(IsPrime, '/<int:num>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')