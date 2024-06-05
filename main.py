from flask import Flask
from routes.home import home_route
from routes.projeto import projeto_route

app = Flask(__name__)

app.register_blueprint(home_route)
app.register_blueprint(projeto_route, url_prefix="/projetos")

app.run(debug=True)