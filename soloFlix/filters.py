from django_filters import rest_framework as filters
from soloFlix.models import Videos, Categoria

class VideoFilter(filters.FilterSet):
    titulo = filters.CharFilter(field_name='titulo', lookup_expr='icontains')
    class Meta:
        model = Videos
        fields = ['titulo',]

class CategoriaFilter(filters.FilterSet):
    nome = filters.CharFilter(field_name='titulo', lookup_expr='icontains')

    class Meta:
        model = Categoria
        fields = ['titulo',]
