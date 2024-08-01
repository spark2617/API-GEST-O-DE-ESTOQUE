from database import db
from sqlalchemy.orm import relationship

class Batch(db.Model):
    __tablename__ = 'batch'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    batch_code = db.Column(db.String(100), nullable=False, unique=True)
    arrival_date = db.Column(db.Date, nullable=False)
    expiration_date = db.Column(db.Date, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    stock_movements = relationship('StrockMovement')

    def to_dict(self):
        return {
        'id': self.id,
        'product_id': self.product_id,
        'code': self.batch_code,
        'arrival_date': self.arrival_date.isoformat() if self.arrival_date else None,
        'expiration_date': self.expiration_date.isoformat() if self.expiration_date else None,
        'quantity': self.quantity,
        'stock_movements': [{
            'id': movement.id,
            'type': movement.type,
            'quantity': movement.quantity,
            'date': movement.date.isoformat() if movement.date else None
        } for movement in self.stock_movements]
    }
