from repositories.curso_repository import CursoRepository
from models.curso_model import CursoModel


"""
Classe de serviço da entidade curso
Esta camada é reponsável pela declaração das funções CRUD
utilizo para instanciar o repositorio da entidade curso 
e para criar as funções de manipulação no Banco
"""

class CursoService:
    def __init__(self):
        # Instanciação do Repositório de Curso
        self.repository = CursoRepository()

    def listar_cursos(self):
        """
        Função para listar todos os cursos cadastrados no banco
        """
        return self.repository.get_all()

    def buscar_curso_por_id(self, curso_id):
        """
        Função para busca especifica pelo ID do Curso, como parametro 
        recebe o ID para consulta
        """
        curso = self.repository.buscar_por_id(curso_id)
        if not curso:
            raise ValueError(f"Curso com o id: {curso_id} não encontrado!!")
        return curso

    def criar_curso (self, nome, codigo):
        """
        Função responsável pela criação de um novo curso
        recebe como parametro o nome e o codigo do curso que deseja cadastrar
        """
        if not nome or not codigo:
            raise ValueError("Nome e codigo são obrigatórios!")
        codigo_formatado = codigo.strip().upper()

        if self.repository.find_by_codigo(codigo_formatado):
            raise ValueError("Impossivel criar o curso, pois o código repassado já existe!")

        novo_curso = CursoModel(
            nome = nome.strip(),
            codigo = codigo_formatado
        )
        return self.repository.criar(novo_curso)

    def excluir_curso(self, curso_id):
        """
        Função responsável pela exclusão de um curso do banco de dados
        como parametro recebe o ID do curso que deseja deletar.
        """

        curso = self.repository.buscar_por_id(curso_id)
        self.repository.deletar(curso)
        print(f"O curso: {curso_id} foi deletado com sucesso")

    def atualizar_curso(self, curso_id, nome, codigo):
        """
        Função responsável pela Atualização de um curso do banco de dados
        como parametro recebe o ID, nome e codigo do curso para atualização.
        """
        try:
            curso_id = int(curso_id)
        except(ValueError, TypeError):
            raise ValueError("ID do curso inválido")

        if not nome or not codigo:
            raise ValueError("Campos 'nome' e 'codigo' são obrigatórios.")

        curso = self.repository.buscar_por_id(curso_id)

        codigo_formatado = codigo.strip().upper()
        existente = self.repository.find_by_codigo(codigo_formatado)

        
        if existente and existente.id != curso_id:
            raise ValueError("Código de curso já em uso por outro registro.")

        curso.nome = nome.strip()
        curso.codigo = codigo_formatado
        self.repository.atualizar(curso)
        return curso