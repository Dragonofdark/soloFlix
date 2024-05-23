from django.db import models
    
class Categoria(models.Model):
    titulo = models.CharField(max_length=50, blank=False, null=False)

    Opcao_1 = 'Azul'
    Opcao_2 = 'Vermelho'
    Opcao_3 = 'Roxo'
    Opcao_4 = 'Laranja'
    Opcao_5 = 'Amarelo'
    Opcao_6 = 'Verde'
    Opcao_7 = 'Preto'
    Opcao_8 = 'Ciano'
    
    Escolhas = [
        (Opcao_1, 'Azul'),
        (Opcao_2, 'Vermelho'),
        (Opcao_3, 'Roxo'),
        (Opcao_4, 'Laranja'),
        (Opcao_5, 'Amarelo'),
        (Opcao_6, 'Verde'),
        (Opcao_7, 'Preto'),
        (Opcao_8, 'Ciano'),
    ]
    cor = models.CharField(max_length=50, choices=Escolhas, blank=False, null=False, default='')

    def __str__(self):
        return self.titulo
    
class Videos(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_DEFAULT, default=1)
    titulo = models.CharField(max_length=100, blank=False, null=False)
    descricao = models.CharField(max_length=180, blank=False, null=False)
    url = models.URLField(null=False, blank=False, default='')

    def __str__(self):
        return self.titulo