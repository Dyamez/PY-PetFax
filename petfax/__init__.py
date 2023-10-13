from flask import Flask # , render_template

# app=Flask(__name__,template_folder='./templates')
from flask_migrate import Migrate

# 'postgresql://postgres:chickboyz@localhost:5432/pet_fax'

def create_app():
    app = Flask(__name__)

    # database config 
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:chickboyz@localhost:5432/pet_fax'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from . import models 
    models.db.init_app(app) 
    # need to fix
    migrate = Migrate(app, models.db)

    @app.route('/')
    def hello():
        return 'Hello, PetFax!'
    
    from .import pet
    app.register_blueprint(pet.bp)

    from .import fact
    app.register_blueprint(fact.bp)

    app.route('/')
    def index():
        return "Hello form petfax"

    
    return app