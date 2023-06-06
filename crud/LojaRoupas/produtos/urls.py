from django.urls import include, path
from rest_framework import routers
from .views import CamisaViewSet, CalcaViewSet, TenisViewSet, CasacoViewSet

router = routers.DefaultRouter()
router.register('camisas', CamisaViewSet)
router.register('calcas', CalcaViewSet)
router.register('tenis', TenisViewSet)
router.register('casacos', CasacoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]