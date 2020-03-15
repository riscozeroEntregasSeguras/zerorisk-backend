from flask_restplus import Api

from .zerorisk_api import api as zerorisk_api
from .user_api import api as user_api
from .order_api import api as order_api


api = Api(
    version="1.0",
    title="Zero Risk API",
    description="An API to manage Zero Risk",
)

api.add_namespace(zerorisk_api)
api.add_namespace(user_api)
api.add_namespace(order_api)
