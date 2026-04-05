from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .models import Product
from Website import auth

views = Blueprint('views', __name__)


@views.route('/')
@login_required
def home():
    return render_template("Home.html", user=current_user)


@views.route('/peripherals/mice')
def mice():
    products = Product.query.filter_by(category='mice').all()
    return render_template("mice.html", user=current_user, products=products)


@views.route('/peripherals/keyboards')
def keyboards():
    products = Product.query.filter_by(category='keyboards').all()
    return render_template("keyboards.html", user=current_user, products=products)


@views.route('/peripherals/headsets')
def headsets():
    products = Product.query.filter_by(category='headsets').all()
    return render_template("headset.html", user=current_user, products=products)


@views.route('/office/keyboards')
def office_keyboards():
    products = Product.query.filter_by(category='office keyboards').all()
    return render_template("office-keyboards.html", user=current_user, products=products)
@views.route('/office/mouse')
def mouse():
    products = Product.query.filter_by(category='office mouses').all()
    return render_template("mouse.html", user=current_user, products=products)
