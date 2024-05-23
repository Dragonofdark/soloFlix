from django.test import TestCase
from soloFlix.models import Categoria

class MeuModeloTeste(TestCase):

    def setUp(self):
        """Cria uma instância de `Categoria` para uso nos testes."""
        self.modelo = Categoria(titulo="Teste", Escolhas="Categoria de testes", cor="Cor de testes")

    def test_criacao_modelo(self):
        """Verifica se o modelo foi criado com sucesso."""
        self.assertEqual(self.modelo.titulo, "Teste")
        self.assertEqual(self.modelo.Escolhas, "Categoria de testes")
        self.assertEqual(self.modelo.cor, "Cor de testes")

    def test_representacao_modelo(self):
        """Verifica se a representação textual do modelo está correta."""
        self.assertEqual(str(self.modelo), "Teste")