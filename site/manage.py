import os
from app import create_app
from flask_script import Manager, Server
from app.main.models import *
import json
import random
import string

app = create_app("dev")
manager = Manager(app)

@app.template_filter('strftime')
def _jinja2_filter_datetime(date, fmt=None):
    return date.strftime('%d, %b %Y %H:%M')

@manager.option("-filename", default="manufacturers.json")
def add_manufacturers(filename):
    try:
        with open(filename) as items_file:
            items = json.loads(items_file.read())

        for item in items:
            if not Manufacturer.objects(name=item['name']):
                manufacturer = Manufacturer(
                    name=item['name'],
                    slug=item['slug'],
                    image_url=item['image_url']
                )
                manufacturer.save()

        print("Manufacturers sucessfully added")
    except Exception as e:
        print(e)

@manager.option("-filename", default="aspenpumps.json")
def add_aspen(filename):
    try:
        with open(filename) as items_file:
            items = json.loads(items_file.read())

        manufacturer = Manufacturer.objects(name="Aspen Pumps").first()

        for item in items:
            if not Product.objects(name=item['name']):
                product = Product(
                    name=item['name'],
                    image_main_url=item['image'],
                    short_description=item['short_description'],
                    killer_features=item['killer_features'],
                    description=item['description'],
                    specifications=item['specifications'],
                    manufacturer_id=str(manufacturer._id),
                    category=item['category']
                )
                product.save()

        print("Products sucessfully added")
    except Exception as e:
        print(e)

def gen_rand_string(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

@manager.command
def add_fake_news():
    for i in range(40):
        p = Post()
        p.title = gen_rand_string()
        p.text = gen_rand_string(random.randint(50, 500))
        p.image_url = "https://www.seniorennet.be/Pages/grappig_schattig/upload/530d1d415d1c5.jpg"
        p.slug = p.title
        p.save()

if __name__ == '__main__':
    manager.run()
