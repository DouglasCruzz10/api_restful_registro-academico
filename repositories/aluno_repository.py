from repositories.base_repository import BaseRepository
from models.aluno_model import AlunoModel


class AlunoRepository(BaseRepository):
    def __init__(self):
        super().__init__(AlunoModel)
    def find_by_matricula(self, matricula):
        return self.model.query.filter_by(matricula=matricula).first()

    def find_by_email(self, email):
        return self.model.query.filter_by(email=email).first()
    
    def find_by_turma(self, turma_id):
        return self.model.query.filter_by(turma_id=turma_id).all()

