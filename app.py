from flask import Flask, request, jsonify, render_template
import sqlite3
from formsql import get_response


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('main.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route("/get", methods=["GET", "POST"])
def respond():
    msg = request.form["msg"]
    response = get_response(msg)
    return str(response)

if __name__ == '__main__':
    app.run(debug=True)

#test
#t = input()
#print(get_response(t))
