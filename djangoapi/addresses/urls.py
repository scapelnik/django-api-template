from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'addresses', views.AddressesModelViewSet)

urlpatterns = [
    # Pozdravna stran
    path('hello/', views.HelloWord.as_view(), name='hello'),
    
    # ViewSet URL-ji (REST framework)
    path('', include(router.urls)),
]


"""
REST API ENDPOINTS:

1. OSNOVNI ENDPOINTI
--------------------
GET  http://localhost:8000/addresses/hello/

2. ADDRESSESMODELVIEWSET (REST FRAMEWORK)
------------------------------------------
GET    http://localhost:8000/addresses/addresses/
GET    http://localhost:8000/addresses/addresses/1/
POST   http://localhost:8000/addresses/addresses/
PUT    http://localhost:8000/addresses/addresses/1/
PATCH  http://localhost:8000/addresses/addresses/1/
DELETE http://localhost:8000/addresses/addresses/1/
"""
