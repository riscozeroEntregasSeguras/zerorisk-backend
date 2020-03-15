from flask import Flask
from flask_cors import CORS

import settings
from apis import api

app = Flask(__name__)
cors = CORS(app, resources=settings.CORS_RESOURCES_SETUP)

api.init_app(app)


if __name__ == "__main__":
    app.run(host=settings.API_HOST, port=settings.API_PORT,
            debug=settings.API_DEBUG, ssl_context='adhoc',
            threaded=True)
