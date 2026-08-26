from models.turma_model import TurmaModel
from repositories.base_repository import BaseRepository

class TurmaRepository(BaseRepository):
    def __init__(self):
        super().__init__(TurmaModel)

    def find_by_nome(self, nome):
        return self.model.query.filter_by(nome=nome).first()

    def get_turmas_by_curso(self, curso_id):
        return self.model.query.filter_by(curso_id=curso_id).all()