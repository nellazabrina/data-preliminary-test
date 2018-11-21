import datetime
import json
from peewee import IntegerField, CharField, FloatField, DateTimeField, MySQLDatabase, Model
from playhouse.db_url import connect
from playhouse.shortcuts import model_to_dict, dict_to_model

db = MySQLDatabase('data_preliminary', host='localhost', user="root", password="")

def create_tables():
    global db
    db.connect()
    #create the database before, then the table will be created by peewee
    # safe = True, check the table present or not
    db.create_tables([UserReview], safe=True)
    db.close()

class BaseModel(Model):
    class Meta:
        database = db

class UserReview(BaseModel):
    # id auto create at peewee
    order_id  = IntegerField(unique=True, null=False)
    product_id = IntegerField(null=False) #user could buy same product w/ same id
    user_id = CharField(null=False, max_length=255)
    rating = FloatField(default=0)
    review = CharField(max_length=255, null=True, default=None)
    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField(default=datetime.datetime.now)

    def save(self, *args, **kwargs):
        if self.rating < 1 or self.rating > 5:
            raise ValueError('"rating" must be between 1 and 5')
        self.updated_at = datetime.datetime.now()
        return super(UserReview, self).save(*args, **kwargs)

    def as_json(self):
        return json.dumps(model_to_dict(self), default = self._json_encoder)

    def _json_encoder(self, o):
        if isinstance(o, datetime.datetime):
            return o.__str__()
        else:
            return json.dumps(o)

    class Meta:
        table_name = "UserReview"

create_tables()
