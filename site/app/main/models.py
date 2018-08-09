from .. import db
# from . import send_mail
from flask_login import UserMixin
import datetime
from .send_mail import send_email

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

class Message(db.Document):
    _id = db.SequenceField()
    name = db.StringField(default="")
    email = db.StringField(default="")
    phone = db.StringField(default="")
    topic = db.StringField(default="")
    text = db.StringField(default="")

    def send(self):
        self.save()
        try:
            message_body = 'Имя: %s\nemail: %s\nТелефон: %s\nТема: %s\nСообщение:\n%s' % (self.name, self.email, self.phone, self.topic, self.text)
            send_email("sergeenkov.michael@gmail.com", "Новое сообщение с сайта engineerss.ru", message_body)
        except Exception as e:
            print(e)

class Post(db.Document):
    _id = db.SequenceField()
    title = db.StringField(default="")
    text = db.StringField(default="")
    slug = db.StringField(default="")
    date = db.DateTimeField(default=datetime.datetime.now)
    category = db.StringField(default="Новости")
    tags = db.ListField(default=[])
    image_url = db.StringField(default="")

class Tag(db.Document):
    _id = db.SequenceField()
    tag = db.StringField(default="")
