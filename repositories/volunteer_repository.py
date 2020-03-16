from models.postgres.tables import Volunteer


class VolunteerRepository:
    def __init__(self, volunteer_database: Volunteer):
        self.volunteer_database = volunteer_database

    def add_volunteer(self):
        pass

    def get_volunteer(self):
        pass

    def get_all_volunteers(self):
        pass
