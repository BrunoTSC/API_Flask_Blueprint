dados = {
    "professores": [  
        {"id":1, "nome":"Kleber", "idade":26, "matéria":"DevOps", "observações": None},
        {"id":2, "nome":"Caio", "idade":24, "matéria":"APIs", "observações": None},
        {"id":3, "nome":"Beicinho", "idade":28, "matéria":"Lógica de programação", "observações": None},
        {"id":4, "nome":"Larissa", "idade":25, "matéria":"Soft Skills", "observações": None},
        ],
}

class ProfessorNaoEncontrado(Exception):
    pass

def professor_por_id(id_professor):
    lista_professores = dados['professores']
    for dicionario in lista_professores:
        if dicionario['id'] == id_professor:
            return dicionario
    raise ProfessorNaoEncontrado

def listar_professores():
    print("Dados carregados:", dados)  
    return dados['professores']

def adicionar_professor(professor):
    dados['professores'].append(professor)

def atualizar_professor(id_professor, novos_dados):
    professor = professor_por_id(id_professor)
    professor.update(novos_dados)

def excluir_professor(id_professor):
    professor = professor_por_id(id_professor)
    dados['professores'].remove(professor)
