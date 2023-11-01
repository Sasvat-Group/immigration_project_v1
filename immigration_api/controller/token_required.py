import jwt
from main import app
from functools import wraps
from flask import request, make_response
from services.UsersMaster_Services import UsersMaster


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = result = ""
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]
        if not token:
            return make_response({"Error": "Authentication Token is missing!"}, 401)
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return make_response({"Error": "Token expired!"}, 401)
        except:
            return make_response({"Error": "Token is invalid!"}, 401)
        result = UsersMaster().getUsersDetailsByName(data['username'])
        if result[2] == 204:
            return make_response({"Error": "Username not found! Unauthorized."}, 401)
        if not result[0]:
            return make_response({"Error": result[1]}, result[2])
        return f(result[1], *args, **kwargs)

    return decorated
