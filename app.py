from flask import Flask
from database import db

from controllers import controllers_bp

app = Flask(__name__)
app.config.from_object('config.Config')

db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(controllers_bp, url_prefix='/api')

if __name__ == "__main__":
    app.run(debug=True)