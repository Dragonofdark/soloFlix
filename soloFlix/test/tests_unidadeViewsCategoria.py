from django.test import TestCase
from rest_framework.test import APIClient
from soloFlix.views import categoriaViewSet

class MeuControllerTeste(TestCase):

    def setUp(self):
        """Cria um cliente API e uma instância do controller."""
        self.cliente = APIClient()
        self.controller = categoriaViewSet()

    def test_lista_objetos(self):
        """Verifica se a API lista todos os objetos."""
        resposta = self.cliente.get('/aluraFlix/')
        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(len(resposta.data), 3)

    def test_recupera_objeto(self):
        """Verifica se a API recupera um objeto específico."""
        resposta = self.cliente.get('/aluraFlix/1/')
        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(resposta.data['nome'], "Objeto 1")

    def test_cria_objeto(self):
        """Verifica se a API cria um novo objeto."""
        dados = {'titulo': 'Nova Categoria', 'Escolhas': 'Categoira de teste', 'cor': 'Cor de teste'}
        resposta = self.cliente.post('/aluraFlix/', dados)
        self.assertEqual(resposta.status_code, 201)
        self.assertEqual(resposta.data['id'], 4)