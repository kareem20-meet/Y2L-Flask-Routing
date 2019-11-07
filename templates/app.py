from flask import Flask, request, url_for, render_template
app = Flask(__name__)
 
@app.route('/')
def index():
    return render_template("home.html")
 
@app.route('/hello')
def hello():
    return render_template("store.html")
 
app.run(debug = True)