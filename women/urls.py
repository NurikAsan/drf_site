from django.urls import path, include
from .api.women_views import WomenViewSet
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'women', WomenViewSet)


urlpatterns = [
    path('api/v1/', include(router.urls))
    # path('women/', WomenViewSet.as_view({'get':'list'})),
    # path('women/<int:pk>/', WomenViewSet.as_view({'put':'update'})),
]