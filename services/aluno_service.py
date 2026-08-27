from repositories.aluno_repository import AlunoRepository
from repositories.turma_repository import TurmaRepository
from models.aluno_model import AlunoModel

class AlunoService:
    def __init__(self):
        self.aluno_repository = AlunoRepository()
        self.turma_repo = TurmaRepository()

    def listar_todos(self, turma_id = None):
        if turma_id:
            try:
                turma_id = int(turma_id)
                return self.aluno_repository.find_by_turma(turma_id)
            except (ValueError, TypeError):
                raise ValueError("ID da turma inválido para filtro.")
        return self.aluno_repository.get_all()

    def buscar_aluno_id(self, aluno_id):
        try:
            aluno_id = int(aluno_id)
        except (ValueError, TypeError):
            raise ValueError("ID do aluno inválido.")

        aluno = self.aluno_repository.buscar_por_id(aluno_id)
        if not aluno:
            raise ValueError ('Aluno não encontrado.')
        return aluno

    def criar_aluno (self, matricula, nome, email, turma_id):
        if not matricula or not nome or not email or not turma_id:
            raise ValueError("Campos 'matricula', 'nome', 'email' e 'turma_id' são obrigatórios.")

        matricula_formatada = str(matricula).strip()
        nome_formatado = nome.strip()
        email_formatado = email.strip()

        try:
            turma_id = int(turma_id)
        except (ValueError, TypeError):
            raise ValueError("O campo 'turma_id' deve ser um número inteiro.")

        # Validações
        if not self.turma_repo.buscar_por_id(turma_id):
            raise ValueError("Não é possível criar o aluno: a Turma informada não existe.")

        if self.aluno_repository.find_by_matricula(matricula_formatada):
            raise ValueError ('Já existe um aluno cadastrado com essa matricula!')

        if self.aluno_repository.find_by_email(email_formatado):
            raise ValueError ('Já existe um aluno cadastrado com esse email!')

        # Novo ALuno
        novo_aluno = AlunoModel(
            matricula = matricula_formatada,
            nome = nome_formatado,
            email = email_formatado,
            turma_id = turma_id
        )
        return self.aluno_repository.criar(novo_aluno)

    def atualizar_aluno(self, aluno_id , matricula, nome, email, turma_id):
        aluno = self.aluno_repository.buscar_por_id(aluno_id)
        if not matricula or not nome or not email or not turma_id:
            raise ValueError("Campos 'matricula', 'nome', 'email' e 'turma_id' são obrigatórios.")
        matricula_formatada = str(matricula).strip()
        nome_formatado = nome.strip()
        email_formatado = email.strip()

        try:
            turma_id = int(turma_id)
        except (ValueError, TypeError):
            raise ValueError("O campo 'turma_id' deve ser um número inteiro.")

        # Validações
        
        if not self.turma_repository.get_by_id(turma_id):
            raise ValueError("Não é possível atualizar: a Turma informada não existe.")

        existente_mat = self.repository.find_by_matricula(matricula_formatada)
        if existente_mat and existente_mat.id != aluno.id:
            raise ValueError("Esta matrícula já pertence a outro aluno.")

        existente_email = self.repository.find_by_email(email_formatado)
        if existente_email and existente_email.id != aluno.id:
            raise ValueError("Este e-mail já pertence a outro aluno.")

        aluno.matricula = matricula_formatada
        aluno.nome = nome_formatado
        aluno.email = email_formatado
        aluno.turma_id = turma_id
        self.aluno_repository.atualizar(aluno)
        return aluno


    def excluir_aluno(self, aluno_id):
        aluno = self.aluno_repository.buscar_por_id(aluno_id)
        self.aluno_repository.deletar(aluno)