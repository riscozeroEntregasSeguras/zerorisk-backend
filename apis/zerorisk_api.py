from flask_restplus import Namespace, Resource

api = Namespace("zerorisk")


@api.route("/status")
class Status(Resource):
    def get(self):
        """Pings the server to ensure it is working as expected"""
        return {'status': 'OK'}
