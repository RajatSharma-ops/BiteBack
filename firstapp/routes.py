from flask import render_template,request,redirect,flash,url_for,session
from flask_bcrypt import Bcrypt
from flask_login import login_user, logout_user,current_user,login_required
from firstapp.models import Donor,User
from firstapp.app import db 
import time


def register_routes(app,db):
    bcrypt = Bcrypt(app)

    @app.context_processor
    def inject_user():
        return dict(current_user=current_user)

    @app.route('/')
    def index():
        if logout_user:
            flash('Logged out successfully.')
        return render_template('index.html')
    
    @app.route('/contact')
    def contact():
        return render_template('contact.html')
    
    @app.route('/donor', methods=['GET', 'POST'])
    @login_required
    def donor():
        if request.method == 'POST':
            name = request.form['name']
            food_item = request.form['food_item']
            quantity = request.form['quantity']
            address = request.form['address']
            if not name or not food_item or not quantity or not address:
                flash("All fields are required.")
                return redirect('/donor')

            new_donor = Donor(name=name, food_item=food_item, quantity=quantity, address=address)
            db.session.add(new_donor)
            db.session.commit()
            return redirect('/receiver')
        return render_template('donor.html')

    @app.route('/receiver')
    def receiver():
        donors = Donor.query.filter_by(is_booked=False).all()
        return render_template('receiver.html', donors=donors)
    

    @app.route('/sign_up', methods=['GET', 'POST'])
    def sign_up():
            if request.method == 'POST':
                name = request.form['U_name']
                email = request.form['U_email']
                raw_password = request.form['password']

        # Check if email already exists
                existing_user = User.query.filter_by(U_email=email).first()
                if existing_user:
                    flash("Email is already in use. Please choose a different one.")
                    return redirect(url_for('sign_up'))

                hashed_password = bcrypt.generate_password_hash(raw_password).decode('utf-8')
                new_user = User(U_name=name, U_email=email, password=hashed_password)
                db.session.add(new_user)
                db.session.commit()
                flash('Signed Up successfully! Please log in.')
                return redirect(url_for('login'))
            return render_template('sign_up.html')
    
    
    # 🔐 Login Route
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == "GET":
            return render_template('sign_up.html')  #since login and signup are in the same page
        elif request.method == 'POST':
            email = request.form['U_email']
            password= request.form['password']
            
            user = User.query.filter(User.U_email == email).first()
            if not user:
                flash('User not found. Please sign up.')
                return redirect(url_for('sign_up'))
            if user and bcrypt.check_password_hash(user.password,password):
                session.permanent = False
                login_user(user)
                session['last_activity']=time.time()
                return redirect(url_for('donor'))
            else:
                flash('either name or password is wrong!!')
                return redirect(url_for('login'))
        


    
          

    # 🔓 Logout Route
    @app.route('/logout')
    @login_required
    def logout(): 
        logout_user()
        flash('Logged out successfully.')
        return redirect(url_for('index'))

    @app.route('/delete/<int:id>', methods=['POST'])
    @login_required
    def delete_donor(id):
        donor = Donor.query.get_or_404(id)
        db.session.delete(donor)
        db.session.commit()
        flash('Donor deleted successfully.')
        return redirect(url_for('receiver'))
    
    from flask import flash, redirect, url_for

    @app.route('/book/<int:donor_id>', methods=['POST'])
    def book_donation(donor_id):
        donor = Donor.query.get_or_404(donor_id)
        if donor.is_booked:
            flash("This donation has already been booked.")
        else:
            donor.is_booked = True
            db.session.commit()
            flash("Booking successful!")
        return redirect(url_for('receiver'))
    