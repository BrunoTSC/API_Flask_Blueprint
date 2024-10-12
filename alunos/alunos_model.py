dados = {
    "alunos": [
        {"id":1, "nome":"Marlon", "idade":21, "turma":"3ºA", "data de nascimento": "18/06/2003", "nota do primeiro semestre":8.0,"nota do segundo semestre":9.0, "média final":8.5},
        {"id":2, "nome":"Bianca", "idade":18, "turma":"3ºB", "data de nascimento": "08/02/2006", "nota do primeiro semestre":7.0,"nota do segundo semestre":8.0, "média final":7.5},
        {"id":3, "nome":"Lucas", "idade":20, "turma":"3ºB", "data de nascimento": "14/11/2004", "nota do primeiro semestre":7.5,"nota do segundo semestre":7.0, "média final":7.25},
        {"id":4, "nome":"João", "idade":22, "turma":"3ºA", "data de nascimento": "23/07/2002", "nota do primeiro semestre":6.0,"nota do segundo semestre":8.0, "média final":7.0},
        {"id":5, "nome":"Katarina", "idade":25, "turma":"3ºA", "data de nascimento": "10/08/1999", "nota do primeiro semestre":5.0,"nota do segundo semestre":9.0, "média final":7.0},
        {"id":6, "nome":"Luiza", "idade":23, "turma":"3ºB", "data de nascimento": "19/12/2001", "nota do primeiro semestre":10.0,"nota do segundo semestre":7.0, "média final":8.5},
    ],
    "professores": []
}

class AlunoNaoEncontrado(Exception):
    pass

def aluno_por_id(id_aluno):
    lista_alunos = dados['alunos']
    for dicionario in lista_alunos:
        if dicionario['id'] == id_aluno:
            return dicionario
    raise AlunoNaoEncontrado

def listar_alunos():
    print("Dados carregados:", dados)  
    return dados['alunos']


def adicionar_aluno(aluno):
    dados['alunos'].append(aluno)

def atualizar_aluno(id_aluno, novos_dados):
    aluno = aluno_por_id(id_aluno)
    aluno.update(novos_dados)

def excluir_aluno(id_aluno):
    aluno = aluno_por_id(id_aluno)
    dados['alunos'].remove(aluno)
