from flask import Flask
from routes.login import login_route
from routes.main import inventario_route
from routes.principal import principal_route

app = Flask(__name__)

app.secret_key = 'wayne'

app.register_blueprint(login_route, url_prefix='/login')

app.register_blueprint(inventario_route, url_prefix='/inventario')

app.register_blueprint(principal_route, url_prefix='/principal')


app.run (debug = True)

