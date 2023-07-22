from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('main.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route("/get", methods=["GET", "POST"])
def respond():
    msg = request.form["msg"]
    #response = chatbot.get_response(msg)
    response = "not there yet"
    return str(response)

if __name__ == '__main__':
    app.run(debug=True)
