from flask_restplus import reqparse
from flask_restplus.reqparse import RequestParser


class UserParser:
    def __init__(self):
        pass

    def get_parser_age(self) -> RequestParser:
        parser = reqparse.RequestParser()
        parser.add_argument(
            "age",
            type=int,
            required=True,
            help="User age"
        )
        return parser
