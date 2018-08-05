from flask import render_template, request, redirect, url_for, abort, current_app, flash
from . import main
from .. import db
from flask import jsonify
from .models import *

@main.route("/")
def index():
    return render_template("main-page.html")

@main.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        return render_template("contact-page.html")
    elif request.method == 'POST':
        try:
            data = request.get_json()
            message = Message(
                name=data['user_name'],
                email=data['user_email'],
                phone=data['user_phone'],
                topic=data['user_topic'],
                text=data['user_mesage']
            )
            message.send()
        except Exception as e:
            print(e)
            abort(500)
        return jsonify({"success": True})    

@main.route("/manufacturers/<string:manufacturer_slug>")
def show_products(manufacturer_slug):
    try:
        manufacturer = Manufacturer.objects(slug=manufacturer_slug).first()
        if not manufacturer:
            abort(404)
        products = Product.objects(manufacturer_id=str(manufacturer._id))
        return render_template('products-page.html', manufacturer=manufacturer, products=products)
    except Exception as e:
        print(e)
        abort(500)

@main.route("/products/<int:product_id>")
def product_detail(product_id):
    product = Product.objects(_id=product_id).first()

    return render_template("product-detail.html", product=product)
