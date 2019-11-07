from flask import Flask, request, url_for, render_template
app = Flask(__name__)
 
@app.route('/home.html')
def index():
    return render_template("home.html")
 
@app.route('/store')
def store():
    return render_template("store.html")
 
app.run(debug = True)