from flask import render_template, request, redirect, url_for
from app import db
from models import Donor



def register_routes(app, db):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/contact', methods=['GET', 'POST'])
    def contact():
        return render_template('contact.html')

    @app.route('/donor', methods=['GET', 'POST'])
    def donor():
        if request.method == 'POST':
            name = request.form['name']
            food_item = request.form['food_item']
            quantity = request.form['quantity']
            address = request.form['address']

            new_donor = Donor(name=name, food_item=food_item, quantity=quantity, address=address)
            db.session.add(new_donor)
            db.session.commit()
            return redirect('/receiver')
        return render_template('donor.html')

    @app.route('/receiver', methods=['GET'])
    def receiver():
        donors = Donor.query.all()
        return render_template('receiver.html', donors=donors) 