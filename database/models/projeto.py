from peewee import Model, CharField, FloatField
from database.database import db

class Divida(Model):
    nome_dividas = CharField()
    valor_divida = FloatField()
    
    class Meta:
        database = db

class Salario(Model):
    salario = FloatField()

    class Meta:
        database = db

class datas(Model):
    data_ini = CharField()
    data_fin = CharField()

    class Meta:
        database = db

