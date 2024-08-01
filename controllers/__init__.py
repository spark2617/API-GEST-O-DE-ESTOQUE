from flask import Blueprint

# Importa os blueprints dos controladores
from .product import product_bp
from .supplier import supplier_bp
from .batch import batch_bp
from .strockMovement import strockMovement_bp
from .category import category_bp

# Cria um blueprint para agrupar todos os controladores
controllers_bp = Blueprint('controllers_bp', __name__)

# Registra os blueprints nos controladores principais com nomes únicos
controllers_bp.register_blueprint(product_bp, name='product_bp')
controllers_bp.register_blueprint(supplier_bp, name='supplier_bp')
controllers_bp.register_blueprint(batch_bp,  name='batch_bp')
controllers_bp.register_blueprint(strockMovement_bp, name='stockMovement_bp')
controllers_bp.register_blueprint(category_bp, name='category_bp')
