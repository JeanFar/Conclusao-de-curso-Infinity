from flask import Blueprint, render_template

principal_route = Blueprint('principal', __name__)

@principal_route.route('/')

def principal():
    return render_template('principal.html')