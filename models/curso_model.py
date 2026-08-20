from database import db

"""
Criação do Modelo "CursoModel" do banco de dados 
com o nome da tabela e as colunas
"""

class CursoModel(db.Model):
    __tablename__ = "cursos_teste"
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100), unique=True, nullable = False)
    codigo = db.Column(db.String(30), unique=True, nullable = False)
