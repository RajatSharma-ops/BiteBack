from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')

@app.route('/donor', methods=['GET', 'POST'])
def donor():
    return render_template('donor.html')


@app.route('/receiver', methods=['GET'])
def receiver():
    return render_template('receiver.html') 