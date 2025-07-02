import os
import time
from flask import Flask,session,flash,url_for,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, current_user, logout_user, login_user
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


db = SQLAlchemy()    
migrate = Migrate()


def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    db.init_app(app) 
    migrate.init_app(app, db)
    bcrypt = Bcrypt(app)
    loginManager = LoginManager(app)
    loginManager.login_view = 'login'  # Redirect here if user not logged in

    from firstapp.models import User
    @loginManager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from firstapp.models import Donor
    from firstapp.routes import register_routes
    register_routes(app,db)
    SESSION_TIMEOUT = 600

    with app.app_context():
        db.create_all()
        print("✅ Tables created or already existed.")

    @app.before_request
    def auto_logout():
        if current_user.is_authenticated:
            now = time.time()
            last_activity = session.get('last_activity')

            if last_activity:
                elapsed = now - last_activity
                if elapsed > SESSION_TIMEOUT:
                    logout_user()
                    session.clear()
                    flash("You have been logged out due to inactivity.")
                    return redirect(url_for('login'))

            session['last_activity'] = now
   
    return app


app = create_app()