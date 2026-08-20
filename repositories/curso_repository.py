from models.curso_model import CursoModel
from repositories.base_repository import BaseRepository

class CursoRepository(BaseRepository):
    def __init__(self):
        super().__init__(CursoModel)

    # Apenas métodos específicos desta entidade
    def find_by_codigo(self, codigo):
        return self.model.query.filter_by(codigo=codigo).first()