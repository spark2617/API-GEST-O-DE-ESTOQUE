from database import db

class StrockMovement(db.Model):
    __tablename__ = 'strockMovement'

    id = db.Column(db.Integer, primary_key=True)
    batch = db.Column(db.Integer, db.ForeignKey('batch.id'), nullable=False)
    movement_type = db.Column(db.String(10), nullable=False)
    movement_date = db.Column(db.DateTime, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)