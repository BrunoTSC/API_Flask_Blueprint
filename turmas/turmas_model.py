dados = {
    "turmas": [  
        {"id":1, "descrição":"3A - DevOps", "professor":"Kleber", "ativo": True},
        {"id":2, "descrição":"3A - APIs", "professor":"Caio", "ativo": True},
        {"id":3, "descrição":"3A - Lógica de programação", "professor":"Beicinho", "ativo": True},
        {"id":4, "descrição":"3A - Soft Skills", "professor":"Gustavo", "ativo": True},
        ],
}

class TurmaNaoEncontrada(Exception):
    pass

def turma_por_id(id_turma):
    lista_turmas = dados['turmas']
    for dicionario in lista_turmas:
        if dicionario['id'] == id_turma:
            return dicionario
    raise TurmaNaoEncontrada

def listar_turmas():
    print("Dados carregados:", dados)  
    return dados['turmas']

def adicionar_turma(turma):
    dados['turmas'].append(turma)

def atualizar_turma(id_turma, novos_dados):
    turma = turma_por_id(id_turma)
    turma.update(novos_dados)

def excluir_turma(id_turma):
    turma = turma_por_id(id_turma)
    dados['turmas'].remove(turma)
