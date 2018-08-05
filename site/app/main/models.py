from .. import db
# from . import send_mail
from flask_login import UserMixin
import datetime

class Manufacturer(db.Document):
    _id = db.SequenceField()
    name = db.StringField(default="")
    image_url = db.StringField(default="")
    slug = db.StringField(default="")

class Product(db.Document):
    _id = db.SequenceField()
    name = db.StringField(default="")
    image_main_url = db.StringField(default="")
    short_description = db.StringField(default="Краткое описание отсутствует")
    killer_features = db.ListField(default=[])
    description = db.StringField(default="Описание отсутствует")
    specifications = db.DictField(default={})
    manuals = db.ListField(default=[])
    category = db.StringField(default="Без категории")
    # manufacturer = db.ReferenceField(Manufacturer, reverse_delete_rule=db.CASCADE)
    manufacturer_id = db.StringField(default="")
