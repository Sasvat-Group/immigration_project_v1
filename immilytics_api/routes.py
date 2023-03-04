from main import app
from flask_restful import Api
from modules.hello import Hello

api = Api(app)


api.add_resource(Hello, "/hello", methods=['GET'])
