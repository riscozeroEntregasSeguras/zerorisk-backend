from models.postgres.tables import Isolated


class IsolatedRepository:
    def __init__(self, isolated_database: Isolated):
        self.isolated_database = isolated_database

    def add_isolated(self):
        pass

    def get_isolated(self):
        pass

    def get_all_isolated(self):
        pass
