from database import db
"""
Criação do Modelo "TurmaModel" do banco de dados 
com o nome da tabela e as colunas
"""
class TurmaModel(db.Model):
    __tablename__ = 'turmas'

    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100), unique = True, nullable = False)
    curso_id = db.Column(db.Integer, db.ForeignKey('cursos.id'), nullable=False)

    # relacionamento com curso
    curso = db.relationship('CursoModel', backref=db.backref('turmas', lazy=True))