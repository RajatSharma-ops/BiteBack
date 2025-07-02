from firstapp.app import create_app,db
from firstapp.models import Donor

flask_app = create_app()
app = flask_app

if __name__ == '__main__':
      with flask_app.app_context():
            db.create_all()
            
      flask_app.run(host='0.0.0.0',debug=True)