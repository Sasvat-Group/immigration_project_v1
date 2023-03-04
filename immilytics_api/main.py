import os
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
CORS(app)

from routes import *

if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host="0.0.0.0", port=5000)
