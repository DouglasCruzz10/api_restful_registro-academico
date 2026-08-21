"""
Classe de renderização das informações
render_single = para renderizar uma turma
render_list = para retornar a lista de turmas
"""

class TurmaView:
    @staticmethod
    def render_single(turma):
        return {
            "id" : turma.id,
            "nome": turma.nome,
            "curso_id": turma.curso_id
        }

    @staticmethod
    def render_list(turmas):
        return [TurmaView.render_single(t)for t in turmas]