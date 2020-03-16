from datetime import datetime

import peewee
from playhouse.postgres_ext import ArrayField

from models.postgres import db


class BaseModel(peewee.Model):
    class Meta:
        database = db


class Volunteer(BaseModel):
    email = peewee.CharField(max_length=320, null=False, index=True)
    country = peewee.CharField(max_length=20, null=False, index=True)
    age = peewee.IntegerField(null=False)

    class Meta:
        db_table = "volunteer"


class Isolated(BaseModel):
    email = peewee.CharField(max_length=320, null=False, index=True)
    country = peewee.CharField(max_length=20, null=False, index=True)
    age = peewee.IntegerField(null=False)

    class Meta:
        db_table = "isolated"


class DetailedInfoPortugal(BaseModel):
    user = peewee.ForeignKeyField(Isolated, backref='detailed_infos')
    tax_number = peewee.IntegerField(null=False)
    citizen_card_number = peewee.CharField(max_length=20, null=False, index=True)

    class Meta:
        db_table = "detailed_info_portugal"


class Order(BaseModel):
    volunteer = peewee.ForeignKeyField(Volunteer, backref='volunteers')
    user = peewee.ForeignKeyField(Isolated, backref='isolated')
    address = peewee.CharField(null=False, index=True)
    order = ArrayField(peewee.CharField, index=False)
    status = peewee.CharField(null=False, index=False)
    updated = peewee.DateTimeField(default=datetime.utcnow, index=True)


db.create_tables([Volunteer, Isolated, DetailedInfoPortugal, Order], safe=True)
