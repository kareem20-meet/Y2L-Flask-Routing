from flask import Flask, request, url_for, render_template
app = Flask(__name__)
 
@app.route('/')
def index():
    return render_template("home.html")


@app.route('/cart')
def cart():
    return render_template("cart.html")


@app.route('/login')
def login():
    return render_template("login.html")



@app.route('/store')
def store():
    return render_template("store.html")
 
app.run(debug = True)