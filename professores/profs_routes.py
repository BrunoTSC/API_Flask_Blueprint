from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from .profs_model import ProfessorNaoEncontrado, listar_professores, professor_por_id, adicionar_professor, atualizar_professor, excluir_professor


professores_blueprint = Blueprint('professores', __name__)


@professores_blueprint.route('/professores', methods=['GET'])
def get_professores():
    professores = listar_professores()
    return render_template("professores.html", professores=professores)


@professores_blueprint.route('/professores/<int:id_professor>', methods=['GET'])
def get_professor(id_professor):
    try:
        professor = professor_por_id(id_professor)
        return render_template('professor_id.html', professor=professor)
    except ProfessorNaoEncontrado:
        return jsonify({'message': 'Professor não encontrado'}), 404


@professores_blueprint.route('/professores/adicionar', methods=['GET'])
def adicionar_prof_page():
    return render_template('criarProfessores.html')


@professores_blueprint.route('/professores', methods=['POST'])
def create_professor():
    nome = request.form['nome']
    idade = request.form['idade']
    materia = request.form['materia']
    observacoes = request.form['observacoes']
    novo_professor = {
        'nome': nome,
        'idade': idade,
        'materia': materia,
        'observacoes': observacoes
    }
    adicionar_professor(novo_professor)
    return redirect(url_for('professores.get_professores'))


@professores_blueprint.route('/professores/<int:id_professor>/editar', methods=['GET'])
def editar_professor_page(id_professor):
    try:
        professor = professor_por_id(id_professor)
        return render_template('professor_update.html', professor=professor)
    except ProfessorNaoEncontrado:
        return jsonify({'message': 'Professor não encontrado'}), 404


@professores_blueprint.route('/professores/<int:id_professor>', methods=['PUT',"POST"])
def update_professor(id_professor):
    print("Dados recebidos no formulário:", request.form)
    try:
        professor = professor_por_id(id_professor)
        nome = request.form['nome']
        idade = request.form['idade']
        materia = request.form['materia']
        observacoes = request.form['observacoes']
        
        professor['nome'] = nome
        professor['idade'] = idade
        professor['materia'] = materia
        professor['observacoes'] = observacoes
        
        atualizar_professor(id_professor, professor)
        return redirect(url_for('professores.get_professor', id_professor=id_professor))
    except ProfessorNaoEncontrado:
        return jsonify({'message': 'Professor não encontrado'}), 404


@professores_blueprint.route('/professores/delete/<int:id_professor>', methods=['DELETE',"POST"])
def delete_professor(id_professor):
    try:
        excluir_professor(id_professor)
        return redirect(url_for('professores.get_professores'))
    except ProfessorNaoEncontrado:
        return jsonify({'message': 'Professor não encontrado'}), 404
