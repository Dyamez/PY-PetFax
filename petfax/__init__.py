from flask import Flask # , render_template

# app=Flask(__name__,template_folder='./templates')

def create_app():
    app = Flask(__name__)

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