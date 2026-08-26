from database import db

class TurmaModel(db.Model):
    __tablename__ = 'turmas'

    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100), unique = True, nullable = False)
    curso_id = db.Column(db.Integer, db.ForeignKey('cursos.id'), nullable=False)