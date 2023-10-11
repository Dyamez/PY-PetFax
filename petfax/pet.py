from flask import Blueprint, render_template 

import json

pets = json.load(open('pets.json', encoding='utf8'))
print(pets)

bp = Blueprint('pet', __name__, url_prefix="/pets") # , template_folder='../templates' 

@bp.route('/')
def index(): 
    return render_template('index.html', pets=pets)  #render_template pets=pets

