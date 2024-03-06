from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .viewsets.articleViewset import articleViewset
from .viewsets.anchoViewset import anchoViewset
from .viewsets.configurationObjectViewset import configurationObjectViewset
from .viewsets.coleccionViewset import coleccionViewset
from .viewsets.designColeccionViewset import designColeccionViewset
from .viewsets.ejeViewset import ejeViewset

router = DefaultRouter()
router.register(r'colecciones', coleccionViewset, basename='coleccion')
router.register(r'configurationObject', configurationObjectViewset)
router.register(r'designcoleccion', designColeccionViewset, basename='designcoleccion')
router.register(r'eje', ejeViewset)
router.register(r'ancho', anchoViewset)
router.register(r'articles', articleViewset, basename='articles')


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]