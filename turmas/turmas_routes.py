from flask import Blueprint, request, jsonify
from .turmas_model import TurmaNaoEncontrada, listar_turmas, turma_por_id, adicionar_turma, atualizar_turma, excluir_turma

turmas_blueprint = Blueprint('turmas', __name__)

@turmas_blueprint.route('/turmas', methods=['GET'])
def get_turmas():
    return jsonify(listar_turmas())

@turmas_blueprint.route('/turmas/<int:id_turma>', methods=['GET'])
def get_turma(id_turma):
    try:
        turma = turma_por_id(id_turma)
        return jsonify(turma)
    except TurmaNaoEncontrada:
        return jsonify({'message': 'Turma não encontrada'}), 404

@turmas_blueprint.route('/turmas', methods=['POST'])
def create_turma():
    data = request.json
    adicionar_turma(data)
    return jsonify(data), 201

@turmas_blueprint.route('/turmas/<int:id_turma>', methods=['PUT'])
def update_turma(id_turma):
    data = request.json
    try:
        atualizar_turma(id_turma, data)
        return jsonify(turma_por_id(id_turma))
    except TurmaNaoEncontrada:
        return jsonify({'message': 'Turma não encontrada'}), 404

@turmas_blueprint.route('/turmas/<int:id_turma>', methods=['DELETE'])
def delete_turma(id_turma):
    try:
        excluir_turma(id_turma)
        return '', 204
    except TurmaNaoEncontrada:
        return jsonify({'message': 'Turma não encontrada'}), 404
