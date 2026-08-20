from database import db

class CursoModel(db.Model):
    __tablename__ = "cursos"
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100), unique=True, nullable = False)
    codigo = db.Column(db.String(30), unique=True, nullable = False)
