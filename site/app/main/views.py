from flask import render_template, request, redirect, url_for, abort, current_app, flash
from . import main
from .. import db
from flask import jsonify
from .models import *

@main.route("/")
def index():
    return render_template("main-page.html")

@main.route("/contact")
def contact():
    return render_template("contact-page.html")

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
