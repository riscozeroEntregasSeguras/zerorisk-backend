from flask_restplus import Namespace, Resource

import settings
from parsers.user_parser import UserParser

api = Namespace("user")
user_parser = UserParser()


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


@api.route("/delete/<path:user_email>", methods=['DELETE'])
class Delete(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @api.response(200, "Success")
    def delete(self):
        """Deletes user account with email"""


@api.route("/age", methods=['GET'])
class Age(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @api.expect(user_parser.get_parser_age())
    @api.response(200, "Success")
    def get(self):
        """Check if a given age is fit for isolated or volunteer"""
        parser = user_parser.get_parser_age()
        args = parser.parse_args()

        if settings.MIN_THRESHOLD_AGE <= args.age <= settings.MAX_THRESHOLD_AGE:
            return {"type": "Volunteer"}
        else:
            return {"type": "Isolated"}

