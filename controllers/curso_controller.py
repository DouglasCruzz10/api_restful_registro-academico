import json
from flask import Blueprint, request, jsonify
from views.curso_view import CursoView
from services.curso_service import CursoService

curso_bp = Blueprint('curso_bp', __name__)
curso_service = CursoService()

"""
Declaração dos Endpoints responsáveis pelas funções CRUD
Conexão com o Service para consumir as funções criadas e com a View para renderizar 
as busca indidual ou generalizada
"""

def _extract_json():
    data = request.get_json(silent=True)
    if isinstance(data, str):
        try:
            data = json.loads(data)
        except Exception:
            return None
    return data if isinstance(data, dict) else None




@curso_bp.route('/listar_cursos', methods=['GET'])
def listar():
    cursos = curso_service.listar_cursos()
    return jsonify(CursoView.render_list(cursos)), 200



@curso_bp.route('/buscar_curso/<int:id>', methods=['GET'])
def buscar(id):
    try:
        curso = curso_service.buscar_curso_por_id(id)
        return jsonify(CursoView.render_single(curso)), 200
    except ValueError as err:
        return jsonify({"erro": str(err)}), 404

    

@curso_bp.route('/criar_curso', methods=['POST'])
def criar():
    data = _extract_json() or {}
    try:
        curso = curso_service.criar_curso(
            nome=data.get('nome'),
            codigo=data.get('codigo')
        )
        return jsonify(CursoView.render_single(curso)), 201
    except ValueError as err:
        return jsonify({"erro": str(err)}), 400
    except Exception as err:
        return jsonify({"erro": f"Erro interno: {str(err)}"}), 500

    

@curso_bp.route('/atualizar_curso/<int:id>', methods=['PUT'])
def atualizar(id):
    data = _extract_json() or {}
    try:
        curso = curso_service.atualizar_curso(
            curso_id=id,
            nome=data.get('nome'),
            codigo=data.get('codigo')
        )
        return jsonify(CursoView.render_single(curso)), 200
    except ValueError as err:
        return jsonify({"erro": str(err)}), 400
    except Exception as err:
        return jsonify({"erro": f"Erro interno: {str(err)}"}), 500

    

@curso_bp.route('/excluir_curso/<int:id>', methods=['DELETE'])
def excluir(id):
    try:
        curso_service.excluir_curso(id)
        return jsonify({"mensagem": "Curso excluído com sucesso."}), 200
    except ValueError as err:
        return jsonify({"erro": str(err)}), 400
    except Exception as err:
        return jsonify({"erro": f"Erro interno: {str(err)}"}), 500