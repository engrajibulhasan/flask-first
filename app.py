from flask import Flask
from markupsafe import escape
import re

app = Flask(__name__)


@app.route("/")
def landing_page():
    return "<p>Hello, World!</p>"


@app.route("/hello")
def hello():
    return "<p>Hello route</p>"


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)} '


@app.route('/product/<id>/<int:price>/<int:quantity>')
def handlePrice(id, price, quantity):

    if (quantity > 0):
        total = price*quantity
        return f'Product ID: {escape(id)} and price is:  {escape(price)} || price type: {escape(type(price))} ::::: Total: {escape(total)}'
    else:
        return 'Quantity must be 1 or more'
# API: base_url/product/product-id/unit-price/quantity


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    pathArray = subpath.split("/")
    items = ""
    for item in pathArray:
        items += "\n #Item:"+item

    # show the subpath after /path/
    return f'{"<b>Yes! it is Version 2.0</b>" if re.search("v2", subpath) != None else "" } Subpath {escape(subpath)}, All are::: {escape(items)}'


@app.route("/user-id/<uuid:userId>")
def handleUuid(userId):
    return f'User ID dfdfdf'
# UUID::: 98adfb9d-8180-461c-80f7-1e2d6122c42d


@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/about')
def about():
    return 'The about page'
