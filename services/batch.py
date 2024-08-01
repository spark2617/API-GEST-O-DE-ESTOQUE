from database import db
from services.strockMovement import StrockMovementService
from models.batch import Batch

class BatchService:
    
    @staticmethod
    def get_all_batches():
        return Batch.query.all()
    
    @staticmethod
    def get_batch_by_id(batch_id):
        return Batch.query.get(batch_id)
    
    @staticmethod
    def create_batch(product_id, batch_code, arrival_date, expiration_date, quantity):
        new_batch = Batch(product_id=product_id, batch_code=batch_code, arrival_date=arrival_date, expiration_date=expiration_date, quantity=quantity)
        db.session.add(new_batch)
        db.session.commit()

        StrockMovementService.create_stock_movement(new_batch.id, "ENTRADA", quantity, arrival_date,)
        return new_batch
    
    @staticmethod
    def update_batch(batch_id, product_id=None, batch_code=None, arrival_date=None, expiration_date=None, quantity=None):
        batch = Batch.query.get(batch_id)

        if batch:
            if product_id:
                batch.product_id = product_id
            if batch_code:
                batch.batch_code = batch_code
            if arrival_date:
                batch.arrival_date = arrival_date
            if expiration_date:
                batch.expiration_date = expiration_date
            if quantity:
                batch.quantity = quantity
            db.session.commit()

        return batch
    
    @staticmethod
    def batchEntryOrExit(batch_id, quantity=None):
        batch = Batch.query.get(batch_id)
        if batch:
            if quantity > batch.quantity:
                StrockMovementService.create_stock_movement(batch.id, "ENTRADA", quantity, batch.arrival_date,)
            if quantity < batch.quantity:
                StrockMovementService.create_stock_movement(batch.id, "SAÍDA", quantity, batch.arrival_date,)
            if quantity == batch.quantity:
                return "quantidade igual a quantidade armazenada"
            
            batch.quantity = quantity
            db.session.commit()

            return batch

    
    @staticmethod
    def delete_batch(batch_id):
        batch = Batch.query.get(batch_id)
        if batch:
            db.session.delete(batch)
            db.session.commit()
        return batch
