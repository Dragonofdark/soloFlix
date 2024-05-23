from rest_framework import serializers
from soloFlix.models import Videos, Categoria
from soloFlix.validators import *
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from soloFlix.models import Videos

class categoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

    def validate(self, data):
        if not titulo_valido(data['titulo']):
            raise serializers.ValidationError({'titulo': 'Este campo não pode ter números'})
        return data 

class videoSerializer(serializers.ModelSerializer):
    categoria = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all())
    class Meta:
        model = Videos
        fields = ['id', 'titulo', 'categoria', 'descricao', 'url']

    def validate(self, data):
        if not url_valido(data['url']):
            raise serializers.ValidationError({'url':'Este campo só pode ser preenchido com links'})
        return data 

@api_view(['POST'])
def login(request):
            usuario = request.data.get('Nome de Usuario')
            senha = request.data.get('Senha')

            if not usuario or not senha:
                return Response({'erro': 'Informe usuário e senha'}, status=status.HTTP_400_BAD_REQUEST)

            try:
                user = User.objects.get(usuario=usuario)
            except User.DoesNotExist:
                return Response({'erro': 'Usuário não encontrado'}, status=status.HTTP_401_UNAUTHORIZED)

            if not user.check_password(senha):
                return Response({'erro': 'Senha incorreta'}, status=status.HTTP_401_UNAUTHORIZED)
            
            return Response({'mensagem': 'Usuário autenticado com sucesso!'})

    # Rota protegida para usuários cadastrados (exemplo: obter um vídeo)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def obter_video(request, video_id):
    try:
        video = Videos.objects.get(pk=video_id)
    except Videos.DoesNotExist:
        return Response({'erro': 'Vídeo não encontrado'}, status=status.HTTP_404_NOT_FOUND)

    # Verifica se o usuário pode acessar o vídeo
    if not video.livre and request.user != video.usuario:
        return Response({'erro': 'Permissão negada'}, status=status.HTTP_403_FORBIDDEN)

    return Response(video.serialize())

    # Rota para vídeos livres (apenas GET)
@api_view(['GET'])
def obter_videos_livres(request):
    videos_livres = Videos.objects.filter(livre=True)
    return Response([video.serialize() for video in videos_livres])

    # Rota protegida para usuários cadastrados (exemplo: editar vídeo)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def editar_video(request, video_id):
    try:
        video = Videos.objects.get(pk=video_id)
    except Videos.DoesNotExist:
        return Response({'erro': 'Vídeo não encontrado'}, status=status.HTTP_404_NOT_FOUND)

        # Verifica se o usuário pode editar o vídeo
    if not video.livre and request.user != video.usuario:
        return Response({'erro': 'Permissão negada'}, status=status.HTTP_403_FORBIDDEN)

        # Atualiza os dados do vídeo e salva no banco de dados
    if video.livre and request.user == video.usuario:
        video.save()
        return Response({'mensagem': 'Vídeo editado com sucesso'})

    # Rota protegida para administradores (exemplo: excluir vídeo)
@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def excluir_video(video_id):
    try:
        video = Videos.objects.get(pk=video_id)
    except Videos.DoesNotExist:
        return Response({'erro': 'Vídeo não encontrado'}, status=status.HTTP_404_NOT_FOUND)

    video.delete()
    return Response({'mensagem': 'Vídeo excluído com sucesso'})