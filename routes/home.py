from flask import Blueprint, render_template
from dados.dados import datas, dinheiro, divida
from database.models.projeto import Salario

home_route = Blueprint('home', __name__)

@home_route.route('/')
def home():

    data_labels = [row for row in datas]

    dinheiro_values = [int(Salario.salario.value) for _ in datas] * len(datas)

    data_values = [x - y for x, y in zip(dinheiro_values, divida)]

    divida_values = [row for row in divida]

    print(dinheiro_values)
    print(divida_values)
    print(data_labels)
    return render_template("index.html", data_labels = data_labels, data_values = data_values, dinheiro_values = dinheiro_values, divida_values= divida_values)