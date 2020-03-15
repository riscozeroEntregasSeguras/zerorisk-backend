from flask_restplus import Namespace, Resource

api = Namespace("user")


@api.route("/access_token/<path:user_email>", methods=['GET'])
class AccessToken(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @api.response(200, "Success")
    def get(self, user_email):
        """Gets the access token from user email"""


@api.route("/get/<path:access_token>", methods=['GET'])
class Info(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @api.response(200, "Success")
    def get(self):
        """Gets user info from access token"""


@api.route("/create/<path:user_email>", methods=['PUT'])
class Create(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @api.response(200, "Success")
    def put(self):
        """Creates user account with email"""
