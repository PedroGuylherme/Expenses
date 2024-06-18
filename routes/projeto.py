from flask import Blueprint, render_template, request
from dados.dados import datas, dinheiros, dinheiro, dividas, divida
from datetime import datetime
from database.models.projeto import Salario, Divida

projeto_route = Blueprint('projeto', __name__)

# DINHEIRO
@projeto_route.route('/dinheiro')
def dinheiro_projeto():
    return render_template('dinheiro.html')

@projeto_route.route('/dinheiro', methods=['POST'])
def add_dinheiro_projeto():

    data = request.json
    print(data)

    din = Salario.create(
        salario = data['dinheiro']
    )

    '''din = {
        'dinheiro': f'dinheiro {len(dinheiros) + 1}',
        'R$': int(data['dinheiro'])
    }

    dinheiros.append(din)

    dinheiro.clear()
    if din['R$'] >= 1:  
        dinheiro.append(din['R$'])
    '''
    print(din)
    print(dinheiros,'SDADASDa')
    return render_template('dinheiro.html', din = din)
    
@projeto_route.route('/<int>:dinheiro>/edit')
def edit_dinheiro_projeto():
    
    dinheiro = None
    for c in dinheiro:
        dinheiro = c

    return render_template('dinheiro.html', dinheiro = dinheiro)

# DIVIDA
@projeto_route.route('/divida')
def divida_projeto():

    return render_template('divida.html')

@projeto_route.route('/divida', methods=['POST'])
def add_divida_projeto():
    
    data = request.json
    if data['divida'] == '':
        data['divida'] = '0,0'
    
    data = {
        'nome divida': data['nome divida'], 
        'divida': float(data['divida'].replace(',','.')),
        'dateini': data['dateini'],
        'datefim': data['datefin']
    }
    # diciona valor da divida
    if data['divida'] >= 1:
        dividas.append(data)
    else:
        print('numero não valido')
    
    # Definição das dívidas

    inicio = dividas[0]['dateini']
    fim = dividas[0]['datefim']
    for i in dividas:
        end = i["datefim"]
        start = i['dateini']
        if end > fim:
            fim = end
        if start < inicio:
            inicio = start

    dateini = datetime.strptime(inicio, '%Y-%m-%d')
    datefin = datetime.strptime(fim, '%Y-%m-%d')
    meses = (datefin.year - dateini.year) * 12 + datefin.month - dateini.month + 1
    # achar o valor do numero que de mais alto
    print(meses,'diferença de meses')  
    print(dateini.month,'menor data')
    print(datefin.month,'maior data')

    # Função para calcular a soma das dívidas em um determinado mês
    def soma_dividas_por_mes(mes):
        total_dividas = 0
        for i in dividas:
            inicio_divida = i["dateini"]
            fim_divida = i["datefim"]
            valor_divida = i["divida"]
            print(inicio_divida,'inicio da divida loop')
            print(fim_divida,'fim da divida loop')
            print(valor_divida,' valor da didivda loop')
            print(mes,'valor do mês no loop')
            # Verifica se a dívida está ativa no mês fornecido
            if inicio_divida <= mes <= fim_divida:
                print('entrou no if')
                total_dividas += valor_divida
        
        return total_dividas

    # Calcular a soma das dívidas para cada mês
    i = 0
    divida.clear()
    datas.clear()
    ano = 0
    for mes in range(dateini.month - 1,dateini.month + meses - 1):  # cacula o inicio da divida até o final
        print(mes,'VE ES TA ANTES DO LOOP')
        mes %= 12
        mes += 1
        print('-_'*50)
        print(ano,'ano')
        print(mes,' loop mes ')
        i += 1
        print(i,'quantidade de loop')
        print('-_'*50)
        mes_str = f"{dateini.year + ano}-{mes:02d}-{dateini.day:02d}"
        divida_mes = soma_dividas_por_mes(mes_str)
        print(f"Dívida total em {mes_str}: R$ {divida_mes}")
        divida.append(divida_mes)
        datas.append(f"{dateini.day:02d}-{mes:02d}-{dateini.year + ano}")
        if mes == 12:
            ano += 1
        
        
    print(dividas,'print dividas')
    print(divida,'print divida')
    return render_template('divida.html')

@projeto_route.route('/sobra')
def sobra():

    pass