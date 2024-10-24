from config import db

class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    turma_id = db.Column(db.Integer, db.ForeignKey('turma.id'), nullable=False)
    nota_primeiro_semestre = db.Column (db.Float, nullable=True)
    nota_segundo_semestre = db.Column (db.Float, nullable=True)
    media_final = db.Column(db.Float, nullable=True)
    turma = db.relationship('Turma', backref ='alunos')


    def __init__(self, nome, idade, turma_id, data_nascimento):
        self.nome = nome
        self.idade = idade
        self.turma_id = turma_id
        self.data_nascimento = data_nascimento

    def to_dict(self):
        return {'id': self.id, 'nome': self.nome, 'idade': self.idade, 'turma_id': self.turma_id, 'data_nascimento': self.data_nascimento}

class AlunoNaoEncontrado(Exception):
    pass

def aluno_por_id(id_aluno):
    aluno = Aluno.query.get(id_aluno)
    if not aluno:
        raise AlunoNaoEncontrado
    return aluno.to_dict()

def listar_alunos():
    alunos = Aluno.query.all()
    return [aluno.to_dict() for aluno in alunos]

def adicionar_aluno(aluno_data):
    novo_aluno = Aluno(
        nome=aluno_data['nome'],
        idade=aluno_data['idade'],
        turma_id=aluno_data['turma_id'],
        data_nascimento=aluno_data['data_nascimento'],
        nota_primeiro_semestre=aluno_data.get('nota_primeiro_semestre'),
        nota_segundo_semestre=aluno_data.get('nota_segundo_semestre'),
        media_final=aluno_data.get('media_final')
        )
    db.session.add(novo_aluno)
    db.session.commit()

def atualizar_aluno(id_aluno, novos_dados):
    aluno = Aluno.query.get(id_aluno)
    if not aluno:
        raise AlunoNaoEncontrado
    aluno.nome = novos_dados['nome']
    aluno.idade = novos_dados.get('idade', aluno.idade)
    aluno.turma_id = novos_dados.get('turma_id', aluno.turma_id)
    aluno.data_nascimento = novos_dados.get('data_nascimento', aluno.data_nascimento)
    aluno.nota_primeiro_semestre = novos_dados.get('nota_primeiro_semestre', aluno.nota_primeiro_semestre)
    aluno.nota_segundo_semestre = novos_dados.get('nota_segundo_semestre', aluno.nota_segundo_semestre)

    # Atualizar a média final se as notas estiverem presentes
    if aluno.nota_primeiro_semestre is not None and aluno.nota_segundo_semestre is not None:
        aluno.media_final = (aluno.nota_primeiro_semestre + aluno.nota_segundo_semestre) / 2
    else:
        aluno.media_final = None  # Define como None se as notas não estiverem completas

    db.session.commit()

def excluir_aluno(id_aluno):
    aluno = Aluno.query.get(id_aluno)
    if not aluno:
        raise AlunoNaoEncontrado
    db.session.delete(aluno)
    db.session.commit()