from routes.home import home_route
from routes.projeto import projeto_route
from database.database import db
from database.models.projeto import Salario, datas, Divida

def configure_all(app):
    configure_routes(app)
    configure_db()

def configure_routes(app):
    app.register_blueprint(home_route)
    app.register_blueprint(projeto_route, url_prefix='/clientes') 

def configure_db():
    db.connect()
    db.create_tables([Salario, datas, Divida])