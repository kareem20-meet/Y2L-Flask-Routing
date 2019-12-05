from flask import Flask, request, url_for, render_template
from databases import *
app = Flask(__name__)
 
@app.route('/')
def index():
    return render_template("home.html")


@app.route('/cart')
def cart():
    cr = add_product()
    return render_template("cart.html", cart = cr)


@app.route('/login')
def login():
    return render_template("login.html")



@app.route('/store')
def store():
    pr =  query_all()
    return render_template("store.html", product = pr)


 
app.run(debug = True)