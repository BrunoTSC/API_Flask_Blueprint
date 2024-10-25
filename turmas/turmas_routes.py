from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from .turmas_model import TurmaNaoEncontrada, listar_turmas, turma_por_id, adicionar_turma, atualizar_turma, excluir_turma


turmas_blueprint = Blueprint('turmas', __name__)


@turmas_blueprint.route('/turmas', methods=['GET'])
def get_turmas():
    turmas = listar_turmas()
    return render_template("turmas.html", turmas=turmas)


@turmas_blueprint.route('/turmas/<int:id_turma>', methods=['GET'])
def get_turma(id_turma):
    try:
        turma = turma_por_id(id_turma)
        return render_template('turma_id.html', turma=turma)
    except TurmaNaoEncontrada:
        return jsonify({'message': 'Turma não encontrada'}), 404


@turmas_blueprint.route('/turmas/adicionar', methods=['GET'])
def adicionar_turma_page():
    return render_template('criarTurmas.html')


@turmas_blueprint.route('/turmas', methods=['POST'])
def create_turma():
    descricao = request.form['descricao']
    professor_id = request.form['professor_id']
    ativo = request.form['ativo']
    nova_turma = {
        'descricao': descricao,
        'professor_id': professor_id,
        'ativo': ativo
    }
    adicionar_turma(nova_turma)
    return redirect(url_for('turmas.get_turmas'))


@turmas_blueprint.route('/turmas/<int:turma_id>/editar', methods=['GET'])
def editar_turma_page(turma_id):
    try:
        turma = turma_por_id(turma_id)
        return render_template('turma_update.html', turma=turma)
    except TurmaNaoEncontrada:
        return jsonify({'message': 'Turma não encontrada'}), 404


@turmas_blueprint.route('/turmas/<int:id_turma>', methods=['PUT',"POST"])
def update_turma(id_turma):
    print("Dados recebidos no formulário:", request.form)
    try:
        turma = turma_por_id(turma_id)
        descricao = request.form['descricao']
        professor_id = request.form['professor_id']
        ativo = request.form['ativo']
        
        turma['descricao'] = descricao
        turma['professor_id'] = professor_id
        turma['ativo'] = ativo
        atualizar_turma(id_turma, turma)
        return redirect(url_for('turmas.get_turma', id_turma=id_turma))
    except TurmaNaoEncontrada:
        return jsonify({'message': 'Turma não encontrada'}), 404


@turmas_blueprint.route('/turmas/<int:id_turma>', methods=['DELETE'])
def delete_turma(id_turma):
    try:
        excluir_turma(id_turma)
        return redirect(url_for('turmas.get_turmas'))
    except TurmaNaoEncontrada:
        return jsonify({'message': 'Turma não encontrada'}), 404
