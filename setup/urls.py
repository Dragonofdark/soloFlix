from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from soloFlix.views import videoViewSet, categoriaViewSet, videosGratisViewSet

router = routers.DefaultRouter()
router.register('categorias', categoriaViewSet, basename='Categoria')
router.register('videos', videoViewSet, basename='Videos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('videos/free/', videosGratisViewSet.as_view()),
]
