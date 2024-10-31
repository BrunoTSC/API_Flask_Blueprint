import unittest
from app import app, db  # Importando a app e db do app.py
from alunos.alunos_model import adicionar_aluno, AlunoNaoEncontrado  # Certifique-se de que o caminho está correto
from alunos.alunos_routes import alunos_blueprint

class TestAlunosRoutes(unittest.TestCase):
    @classmethod
    def testConfig(tc):
        tc.app = app
        tc.app.config['TESTING'] = True  # Ativa o modo de teste
        tc.client = tc.app.test_client()
        
        with tc.app.app_context():
            db.create_all()  # Cria o banco de dados para os testes

            # Adiciona um aluno de teste
            tc.aluno_teste = {
                'nome': 'Aluno Teste',
                'idade': 20,
                'turma_id': 1,
                'data_nascimento': '2003-01-01',
                'nota_primeiro_semestre': 7.5,
                'nota_segundo_semestre': 8.0
            }
            adicionar_aluno(tc.aluno_teste)

    @classmethod
    def novoTest(nt):
        with nt.app.app_context():
            db.drop_all()  # Remove o banco de dados após os testes

    def test_get_alunos(self):
        response = self.client.get('/alunos')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Lista de Alunos', response.data)  # Altere conforme necessário para verificar o conteúdo da página

    def test_get_aluno_existente(self):
        response = self.client.get('/alunos/1')  # Supondo que o ID do aluno teste seja 1
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Aluno Teste', response.data)  # Verifica se o nome do aluno está na resposta

    def test_get_aluno_inexistente(self):
        response = self.client.get('/alunos/999')  # ID que não existe
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, {'message': 'Aluno não encontrado'})

    def test_create_aluno(self):
        response = self.client.post('/alunos', data={
            'nome': 'Novo Aluno',
            'idade': '21',
            'turma_id': '1',
            'data_nascimento': '2002-01-01',
            'nota_primeiro_semestre': '8.0',
            'nota_segundo_semestre': '9.0'
        })
        self.assertEqual(response.status_code, 302)  # Redirecionamento após criação
        self.assertEqual(response.location, '/alunos')  # Verifica o redirecionamento correto

    def test_update_aluno_existente(self):
        response = self.client.post('/alunos/1', data={
            'nome': 'Aluno Atualizado',
            'idade': '22',
            'turma_id': '1',
            'data_nascimento': '2001-01-01',
            'nota_primeiro_semestre': '8.5',
            'nota_segundo_semestre': '9.5'
        })
        self.assertEqual(response.status_code, 302)  # Redirecionamento após atualização
        self.assertEqual(response.location, '/alunos/1')

    def test_delete_aluno_existente(self):
        response = self.client.post('/alunos/delete/1')
        self.assertEqual(response.status_code, 302)  # Redirecionamento após deleção
        self.assertEqual(response.location, '/alunos')

    def test_delete_aluno_inexistente(self):
        response = self.client.post('/alunos/delete/999')  # ID que não existe
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, {'message': 'Aluno não encontrado'})

if __name__ == '__main__':
    unittest.main()
