from repositories.turma_repository import TurmaRepository
from repositories.curso_repository import CursoRepository
from models.turma_model import TurmaModel


class TurmaService:
    def __init__(self):
        self.turma_repo = TurmaRepository()
        self.curso_repo = CursoRepository()

    def listar_turmas(self):
        """
        Função para listar todas as turmas cadastradas no banco
        """
        return self.turma_repo.get_all()

    def busca_turma_por_id(self, turma_id):
        """
        Função para busca especifica pelo ID da Turma, como parametro 
        recebe o ID para consulta
        """
        turma = self.turma_repo.buscar_por_id(turma_id)
        if not turma:
            raise ValueError(f"Turma com ID {turma_id} não encontrada.")
        return turma

    def criar_turma(self, nome, curso_id):
        """
        Função responsável pela criação de uma nova turma
        recebe como parametro o nome da turma e o id do curso que deseja cadastrar
        """
        # 1 Regra - Cada nome de turma é unico, não pode haver duas turmas com o mesmo nome
        if self.turma_repo.find_by_nome(nome):
            raise ValueError("Turma já cadastrada!")
        # 2 Regra - validar se o curso informado existe
        if not self.curso_repo.buscar_por_id(curso_id):
            raise ValueError("Curso informado não existe!")
        if not nome:
            raise ValueError("O nome é obrigatório, insira!")
        nova_turma = TurmaModel(
            nome=nome, 
            curso_id=curso_id
            )
        return self.turma_repo.criar(nova_turma)


    def excluir_turma(self, turma_id):
        turma = self.turma_repo.buscar_por_id(turma_id)
        if not turma:
            raise ValueError(f"Turma com ID {turma_id} não encontrada.")
        self.turma_repo.deletar(turma)
        print(f"A turma: {turma_id} foi deletada com sucesso")

    def atualizar_turma(self, turma_id, nome, curso_id):
        turma = self.turma_repo.buscar_por_id(turma_id)
        if not turma:
            raise ValueError(f"Turma com ID {turma_id} não encontrada.")
        # 1 Regra - Cada nome de turma é unico, não pode haver duas turmas com o mesmo nome
        turma_existente = self.turma_repo.find_by_nome(nome)
        if turma_existente and turma_existente.id != turma_id:
            raise ValueError("Turma já cadastrada!")
        # 2 Regra - validar se o curso informado existe
        if not self.curso_repo.buscar_por_id(curso_id):
            raise ValueError("Curso informado não existe!")
        # Atualizar informações 
        turma.nome = nome
        turma.curso_id = curso_id
        self.turma_repo.atualizar(turma)
