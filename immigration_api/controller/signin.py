import datetime
from flask_restful import Resource
from flask import request, make_response
from main import app
from werkzeug.security import generate_password_hash, check_password_hash
from services.UsersMaster_Services import UsersMaster
import jwt


class SignIn(Resource):
    def get(self):
        auth = request.authorization
        if not auth or not auth.username or not auth.password:
            return make_response({"Error": "Username and password are empty."}, 401)

        result = UsersMaster().getUsersDetailsByName(auth.username)
        if result[2] == 204:
            return make_response({"Error": "Username is incorrect."}, 401)
        if not result[0]:
            return make_response({"Error": result[1]}, result[2])
        
        if check_password_hash(result[1]["Password"], auth.password):
            token = jwt.encode(
                {
                    'id': result[1]["ID"],
                    'username': result[1]["UserMail"],
                    "usertype": result[1]["UserType"],
                    "firstname": result[1]["FirstName"],
                    "lastname": result[1]["LastName"],
                    'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60)
                },
                app.config['SECRET_KEY'])
            return make_response({"token": token}, 200)
        else:
            return make_response({"Error": "Password is incorrect."}, 401)
