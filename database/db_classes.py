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


# class Request(BaseModels):
#     user = ForeignKeyField(User, backref="requests")
#     date = DateTimeField()
#     coins_pair = CharField()
#     curr_cost = FloatField()
#     max_cost = FloatField()
#     min_cost = FloatField()
#
#     def __str__(self) -> str:
#         return (f"{self.date} | {self.coins_pair} | curr_cost: {self.curr_cost}, max_cost: {self.max_cost}, min_cost: "
#                 f"{self.min_cost}")
#
#     class Meta:
#         db_table = "requests"


db.create_tables([User])
