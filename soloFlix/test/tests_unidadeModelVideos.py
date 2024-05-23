from django.test import TestCase
from soloFlix.models import Videos

class MeuModeloTeste(TestCase):

    def setUp(self):
        """Cria uma instância de `Videos para uso nos testes."""
        self.modelo = Videos(titulo="Teste", categoria="Categoria de testes", descricao="Video de testes", url="http://www.exemplo.com")

    def test_criacao_modelo(self):
        """Verifica se o modelo foi criado com sucesso."""
        self.assertEqual(self.modelo.titulo, "Teste")
        self.assertEqual(self.modelo.categoria, "Categoria de testes")
        self.assertEqual(self.modelo.descricao, "Video de testes")
        self.assertEqual(self.modelo.url, "https://www.exemplo.com")

    def test_representacao_modelo(self):
        """Verifica se a representação textual do modelo está correta."""
        self.assertEqual(str(self.modelo), "Teste")