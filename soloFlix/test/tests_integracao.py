from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from soloFlix.models import Videos

class VideoAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_requisicao_get_para_listar_videos(self):
        '''Teste para verificar a requisição GET para listar alunos'''

        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_para_criar_videos(self):
        '''Teste para verificar a requisição POST para criar alunos'''

        data = {
            'nome': 'Aluno de Teste 3',
            'rg': '123456798',
            'cpf': '52235491255',
            'data_nascimento': '2003/03/03',
            'celular': '19 92341-4321',
            'foto': ''
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_put_para_atualizar_videos(self):
        '''Teste para verificar a requisição PUT para atualizar alunos'''
        data = {
            'nome': 'Aluno de Teste 1 atualizado',
            'rg': '123456798',
            'cpf': '52235491255',
            'data_nascimento': '2001/01/01',
            'celular': '19 92341-4322',
            'foto': ''
        }
        response = self.client.put('/alunos/1/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)