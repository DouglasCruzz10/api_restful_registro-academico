class CursoView:
    @staticmethod
    def render_single(curso):
        return {
            "id": curso.id,
            "nome": curso.nome,
            "codigo": curso.codigo,
        }
    @staticmethod
    def render_list(cursos):
        return [CursoView.render_single(c) for c in cursos]