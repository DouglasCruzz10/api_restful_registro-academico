from database import db 

"""
Módulo Base 
para comportar as principais funções do banco de dados
"""

class BaseRepository:
    def __init__(self, model):
        self.model = model
    def get_all(self):
        return self.model.query.all()
    
    def buscar_por_id(self, entity_id):
        return self.model.query.get(entity_id)
    
    def criar(self, entity):
        db.session.add(entity)
        db.session.commit()
        return entity
    
    def atualizar(self, entity):
        db.session.commit()
        return entity
    
    def deletar(self, entity):
        db.session.delete(entity)
        db.session.commit()