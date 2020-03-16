from models.postgres.tables import Order


class OrderRepository:
    def __init__(self, order_database: Order):
        self.order_database = order_database

    def add_order(self):
        pass

    def get_order(self):
        pass

    def get_all_orders(self):
        pass
