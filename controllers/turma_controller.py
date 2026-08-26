import json
from flask import Blueprint, request, jsonify
from utils.utils import _extract_json
from views.turma_view import TurmaView
from services.turma_service import TurmaService

turma_bp = Blueprint('turma_bp', __name__)
turma_service = TurmaService()

@turma_bp.route('/listar_turmas', methods=['GET'])
def listar():
    turmas = turma_service.listar_turmas()
    return jsonify(TurmaView.render_list(turmas)), 200

@turma_bp.route('/buscar_turma/<int:id>', methods=['GET'])
def buscar(id):
    try:
        turma = turma_service.busca_turma_por_id(id)
        return jsonify(TurmaView.render_single(turma)), 200
    except ValueError as err:
        return jsonify({'erro': str(err)}), 404

@turma_bp.route('/criar_turma', methods=['POST'])
def criar():
    data = _extract_json() or {}
    try:
        turma = turma_service.criar_turma(
            nome= data.get('nome'),
            curso_id=data.get('curso_id')
        )
        return jsonify(TurmaView.render_single(turma)), 201
    except ValueError as err:
        return jsonify({"erro": str(err)}), 400
    except Exception as err:
        return jsonify({"erro": f"Erro interno: {str(err)}"}), 500

@turma_bp.route('/atualizar_turma/<int:id>', methods=['PUT'])
def atualizar(id):
    data = _extract_json() or {}
    try:
        turma = turma_service.atualizar_turma(
            turma_id = id, 
            nome = data.get('nome'), 
            curso_id = data.get('codigo')
            )
        return jsonify(TurmaView.render_single(turma)), 200
    except ValueError as err:
        return jsonify({"erro": str(err)}), 400
    except Exception as err:
        return jsonify({"erro": f"Erro interno: {str(err)}"}), 500

@turma_bp.route('/excluir_turma/<int:id>', methods=['DELETE'])
def excluir(id):
    try:
        turma_service.excluir_turma(id)
        return jsonify({"mensagem": "Curso excluído com sucesso."}), 200
    except ValueError as err:
        return jsonify({"erro": str(err)}), 400
    except Exception as err:
        return jsonify({"erro": f"Erro interno: {str(err)}"}), 500