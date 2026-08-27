class AlunoView:
    @staticmethod
    def render_singler(aluno):
        if not aluno:
            return {}
        return {
            "id": aluno.id,
            "matricula": aluno.matricula,
            "nome": aluno.nome,
            "email": aluno.email,
            "turma_id": aluno.turma_id,
            "turma_nome": aluno.turma.nome if aluno.turma else None,
            "curso_nome": aluno.turma.curso.nome if (aluno.turma and aluno.turma.curso) else None
        }
    @staticmethod
    def render_list(alunos):
        if not alunos:
            return []
        return [AlunoView.render_singler(a) for a in alunos]