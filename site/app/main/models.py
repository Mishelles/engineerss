from .. import db
# from . import send_mail
from flask_login import UserMixin
import datetime

class Manufacturer(db.Document):
    _id = db.ObjectIdField()
    name = db.StringField(default="")
    image_url = db.StringField(default="")

class Product(db.Document):
    _id = db.ObjectIdField()
    name = db.StringField(default="")
    image_main_url = db.StringField(default="")
    short_description = db.StringField(default="Красткое описание")
    killer_features = db.ListField(default=[])
    description = db.StringField(default="Описание отсутствует")
    specifications = db.DictField(default={})
    manuals = db.ListField(default=[])
    manufacturer = db.ReferenceField(Manufacturer, reverse_delete_rule=db.CASCADE)
