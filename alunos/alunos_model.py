from config import db
from datetime import datetime

class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    turma_id = db.Column(db.Integer, db.ForeignKey('turma.id'), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    nota_primeiro_semestre = db.Column(db.Float, nullable=True, default=0.0)
    nota_segundo_semestre = db.Column(db.Float, nullable=True, default=0.0)
    media_final = db.Column(db.Float, nullable=True, default=None)
    turma = db.relationship('Turma', backref ='alunos')

    def __init__(self, nome, idade, turma_id, data_nascimento, nota_primeiro_semestre, nota_segundo_semestre, media_final):
        self.nome = nome
        self.idade = idade
        self.turma_id = turma_id
        self.data_nascimento = data_nascimento
        self.nota_primeiro_semestre = nota_primeiro_semestre
        self.nota_segundo_semestre = nota_segundo_semestre
        self.media_final = media_final

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'idade': self.idade,
            'turma_id': self.turma_id,
            'data_nascimento': self.data_nascimento.strftime("%Y-%m-%d"),
            'nota_primeiro_semestre': self.nota_primeiro_semestre,
            'nota_segundo_semestre': self.nota_segundo_semestre,
            'media_final': self.media_final
        }


def media(n1,n2):
    return (n1+n2)/2


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
        nome = aluno_data['nome'],
        idade = aluno_data['idade'],
        turma_id = aluno_data['turma_id'],
        data_nascimento = datetime.strptime(aluno_data['data_nascimento'], '%Y-%m-%d').date(),
        nota_primeiro_semestre = aluno_data['nota_primeiro_semestre'],
        nota_segundo_semestre = aluno_data['nota_segundo_semestre'],
        media_final = media(aluno_data['nota_primeiro_semestre'],aluno_data['nota_segundo_semestre'])
    )
    db.session.add(novo_aluno)
    db.session.commit()


def atualizar_aluno(id_aluno, novos_dados):
    aluno = Aluno.query.get(id_aluno)
    if not aluno:
        raise AlunoNaoEncontrado
    
    aluno.nome = novos_dados['nome']
    aluno.idade = novos_dados['idade']
    aluno.turma_id = novos_dados['turma_id']
    if isinstance(novos_dados['data_nascimento'], str):
        aluno.data_nascimento = datetime.strptime(novos_dados['data_nascimento'], '%Y-%m-%d').date()
    else:
        aluno.data_nascimento = novos_dados['data_nascimento']
    aluno.nota_primeiro_semestre = novos_dados['nota_primeiro_semestre']
    aluno.nota_segundo_semestre = novos_dados['nota_segundo_semestre']
    aluno.media_final = novos_dados['media_final']
    aluno.media_final = media(novos_dados['nota_primeiro_semestre'],novos_dados['nota_segundo_semestre'])
    db.session.commit()


def excluir_aluno(id_aluno):
    aluno = Aluno.query.get(id_aluno)
    if not aluno:
        raise AlunoNaoEncontrado
    db.session.delete(aluno)
    db.session.commit()