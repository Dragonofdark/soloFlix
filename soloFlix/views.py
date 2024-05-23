from rest_framework import viewsets
from django.db.models import Q
from soloFlix.models import Videos, Categoria
from soloFlix.serializer import videoSerializer, categoriaSerializer
from soloFlix.filters import VideoFilter, CategoriaFilter
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

class videoViewSet(viewsets.ModelViewSet):
    serializer_class = videoSerializer
    filter_fields = ['categoria']
    http_method_names = ['get', 'post', 'put', 'patch']
    filter_class = VideoFilter

    def get_queryset(self):
        search_query = self.request.query_params.get('search', None)
        queryset = Videos.objects.all()
        if search_query:
            queryset = queryset.filter(
            Q(titulo__icontains=search_query) | Q(descricao__icontains=search_query)
        )
        return queryset

class categoriaViewSet(viewsets.ModelViewSet):
    serializer_class = categoriaSerializer
    http_method_names = ['get', 'post', 'put', 'patch']
    filter_class = CategoriaFilter
    pagination_class = PageNumberPagination
    
    def get_queryset(self):
        queryset = Categoria.objects.all()
        search_query = self.request.query_params.get('search', None)
        if search_query:
            queryset = queryset.filter(Q(titulo__icontains=search_query) | Q(cor__icontains=search_query))
        return queryset
    
class videosGratisViewSet(APIView):
    pagination_class = PageNumberPagination
    
    def get(self):
        videos = Videos.objects.all()

        serializer = videoSerializer(videos, many=True)

        return Response(serializer.data)