from app import create_app,db
from models import Donor

flask_app = create_app()

if __name__ == '__main__':
      db.create_all()
      flask_app.run(host='0.0.0.0',debug=True) 