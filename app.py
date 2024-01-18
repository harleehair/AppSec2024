# app.py
from urllib import request

from flask import Flask, render_template, request

app = Flask(__name__)

contact_forms = []

@app.route('/')
def index():
    # title = "Duck Duck Gööse"
    return render_template('index.html')


@app.route('/about')
def about():
    # title = "About Duck Duck Gööse"
    return render_template("about.html")


@app.route('/contact')
def contact():
    # title = "Contact Ducks"
    return render_template("contact.html")


@app.route('/form', methods=["POST"])
def form():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    if not name or not email or not message:
        error_statement = "All Form Fields Required..."
        return render_template('contact.html',
                               error_statement=error_statement,
                               name=name,
                               email=email,
                               message=message)

    contact_forms.append(f"{name} <{email}>: {message}")
    # title = "Quack!"
    return render_template("form.html", contact_forms=contact_forms)
