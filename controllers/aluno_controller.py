from flask import Blueprint, request, jsonify
from services.aluno_service import AlunoService
from views.aluno_view import AlunoView
from utils.utils import _extract_json

aluno_bp = Blueprint('aluno_bp', __name__)
aluno_service = AlunoService()

@aluno_bp.route('/listar_alunos', methods=['GET'])
def listar():
    turma_id = request.args.get('turma_id', type=int)
    try:
        alunos = aluno_service.listar_todos(turma_id=turma_id)
        return jsonify (AlunoView.render_list(alunos)), 200
    except ValueError as err:
        return jsonify({'erro': str(err)}), 400



    

@aluno_bp.route('/buscar_aluno_id/<int:id>',methods=['GET'])
def buscar(id):
    try:
        aluno = aluno_service.buscar_aluno_id(id)
        return jsonify(AlunoView.render_singler(aluno)), 200
    except ValueError as err:
        return jsonify({'erro': str(err)}), 404

    

@aluno_bp.route('/criar_aluno', methods=['POST'])
def criar():
    data = _extract_json() or {}
    try:
        aluno = aluno_service.criar_aluno(
            matricula=data.get('matricula'),
            nome=data.get('nome'),
            email=data.get('email'),
            turma_id=data.get('turma_id')
        )
        return jsonify(AlunoView.render_singler(aluno)), 201
    except ValueError as err:
        return jsonify({'erro': str(err)}), 400
    except Exception as err:
        return jsonify ({"erro": f"Erro interno: {str(err)}"}), 500


    

@aluno_bp.route('/atualizar_aluno/<int:id>', methods=['PUT'])
def atualizar(id):
    data = _extract_json() or {}
    try:
        aluno = aluno_service.atualizar_aluno(
            aluno_id=id,
            matricula=data.get('matricula'),
            nome=data.get('nome'),
            email=data.get('email'),
            turma_id=data.get('turma_id')
        )
        return jsonify(AlunoView.render_singler(aluno)), 200
    except ValueError as err:
        return jsonify({"erro": str(err)}), 400
    except Exception as err:
        return jsonify({"erro": f"Erro interno: {str(err)}"}), 500


    

@aluno_bp.route('/excluir_aluno/<int:id>', methods=['DELETE'])
def excluir(id):
    try:
        aluno_service.excluir_aluno(id)
        return jsonify({"mensagem": "Aluno excluído com sucesso."}), 200
    except ValueError as err:
        return jsonify({"erro": str(err)}), 400
    except Exception as err:
        return jsonify({"erro": f"Erro interno: {str(err)}"}), 500