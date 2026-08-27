from database import db
"""
Criação do Modelo "AlunoModel" do banco de dados 
com o nome da tabela e as colunas
"""

class AlunoModel(db.Model):
    __tablename__ = 'alunos'

    id = db.Column(db.Integer, primary_key=True)
    matricula = db.Column(db.String(20), unique=True, nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    turma_id = db.Column(db.Integer, db.ForeignKey('turmas.id'), nullable=False)


    # Relacionamento para acessar os dados da turma e curso diretamente via aluno.turma
    turma = db.relationship('TurmaModel', backref=db.backref('alunos', lazy=True))