import os
from app import create_app
from flask_script import Manager, Server
from app.main.models import *
import json

app = create_app("dev")
manager = Manager(app)

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

if __name__ == '__main__':
    manager.run()
