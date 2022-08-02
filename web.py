from pickle import TRUE
from flask import Flask,render_template

app = Flask(__name__)


@app.route("/html")
def htlm():
    return render_template('web.html')
@app.route("/about")
def ANiket():
    return "hello"



app.run(debug=True)