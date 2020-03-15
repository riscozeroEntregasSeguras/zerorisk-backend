import peewee

from models.postgres import db


class BaseModel(peewee.Model):
    class Meta:
        database = db


class User(BaseModel):
    email = peewee.CharField(max_length=320, null=False, index=True)
    country = peewee.CharField(max_length=20, null=False, index=True)
    age = peewee.IntegerField(null=False)

    class Meta:
        db_table = "user"


class DetailedInfoPortugal(BaseModel):
    email = peewee.ForeignKeyField(User, backref='detailed_infos')
    tax_number = peewee.IntegerField(null=False)
    citizen_card_number = peewee.CharField(max_length=20, null=False, index=True)

    class Meta:
        db_table = "detailed_info_portugal"


db.create_tables([User, DetailedInfoPortugal], safe=True)
