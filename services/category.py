from database import db
from models.category import Category

class CategoryService:
    
    @staticmethod
    def get_all_categories():
        return Category.query.all()
    
    @staticmethod
    def get_category_by_id(category_id):
        return Category.query.get(category_id)
    
    @staticmethod
    def create_category(name):
        new_category = Category(name=name)
        db.session.add(new_category)
        db.session.commit()
        return new_category
    
    @staticmethod
    def update_category(category_id, name=None):
        category = Category.query.get(category_id)
        if category:
            if name:
                category.name = name
            db.session.commit()
        return category
    
    @staticmethod
    def delete_category(category_id):
        category = Category.query.get(category_id)
        if category:
            db.session.delete(category)
            db.session.commit()
        return category
