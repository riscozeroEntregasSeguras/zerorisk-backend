from flask_restplus import Namespace, Resource

api = Namespace("order")


@api.route("/create", methods=['PUT'])
class Create(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @api.response(200, "Success")
    def post(self):
        """Create an order"""


@api.route("/list/<path:user_email>", methods=['GET'])
class Status(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @api.response(200, "Success")
    def get(self):
        """Get list of all orders from a user"""


@api.route("/status/<path:order_id>", methods=['GET'])
class Status(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @api.response(200, "Success")
    def get(self):
        """Get status from a order"""


@api.route("/cancel/<path:order_id>", methods=['POST'])
class Cancel(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @api.response(200, "Success")
    def post(self):
        """Cancel an active order"""
