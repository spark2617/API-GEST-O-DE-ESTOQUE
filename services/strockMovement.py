from database import db
from models.strockMovement import StrockMovement

class StrockMovementService:
    
    @staticmethod
    def get_all_stock_movements():
        return StrockMovement.query.all()
    
    @staticmethod
    def get_stock_movement_by_id(movement_id):
        return StrockMovement.query.get(movement_id)
    
    @staticmethod
    def create_stock_movement(batch_id, movement_type, quantity, movement_date):
        new_stock_movement = StrockMovement(batch_id=batch_id, movement_type=movement_type, quantity=quantity, movement_date=movement_date)
        db.session.add(new_stock_movement)
        db.session.commit()
        return new_stock_movement
    
    @staticmethod
    def update_stock_movement(movement_id, batch_id=None, movement_type=None, quantity=None, movement_date=None):
        stock_movement = StrockMovement.query.get(movement_id)
        if stock_movement:
            if batch_id:
                stock_movement.batch_id = batch_id
            if movement_type:
                stock_movement.movement_type = movement_type
            if quantity:
                stock_movement.quantity = quantity
            if movement_date:
                stock_movement.movement_date = movement_date
            db.session.commit()
        return stock_movement
    
    
    @staticmethod
    def delete_stock_movement(movement_id):
        stock_movement = StrockMovement.query.get(movement_id)
        if stock_movement:
            db.session.delete(stock_movement)
            db.session.commit()
        return stock_movement
