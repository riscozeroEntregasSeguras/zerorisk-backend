from flask import Flask
from flask_cors import CORS

from apis import api

app = Flask(__name__)
cors = CORS(app, resources={
    r"/*":
        {
            "methods": "OPTIONS",
            "origins": ["http://localhost:8080",
                        "https://zerorisk-webapp.herokuapp.com/#/home'"]
        }
})

api.init_app(app)


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True, ssl_context='adhoc',
            threaded=True)
