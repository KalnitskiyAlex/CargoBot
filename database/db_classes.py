from peewee import *

db = SqliteDatabase("database.db")


class BaseModels(Model):
    class Meta:
        database = db


class User(BaseModels):
    user_id = IntegerField(primary_key=True)
    username = CharField(null=True)
    first_name = CharField()
    last_name = CharField(null=True)

    class Meta:
        db_table = "users"


class Request(BaseModels):
    user = ForeignKeyField(User, backref="requests")
    date = DateTimeField()
    type = CharField()
    invoice = FloatField()
    weight = FloatField()
    volume = FloatField()
    city = CharField()
    unlicense = BooleanField()

    def __str__(self) -> str:
        return (f"{self.user}|{self.date}|{self.type}|{self.invoice}|{self.weight}|{self.volume}|{self.city}"
                f"|{self.unlicense}")

    class Meta:
        db_table = "requests"


db.create_tables([User, Request])
