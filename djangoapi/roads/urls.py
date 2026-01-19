from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'roads', views.RoadsModelViewSet)

urlpatterns = [
    # Pozdravna stran
    path('hello/', views.HelloWord.as_view(), name='hello'),
    
    # Logout
    path('logout/', views.custom_logout_view, name='logout'),
    
    # RoadsView - CRUD operacije
    path('roads_view/selectone/<int:id>/', views.RoadsView.as_view(), name='roads-selectone'),
    path('roads_view/selectall/', views.RoadsView.as_view(), name='roads-selectall'),
    path('roads_view/insert/', views.RoadsView.as_view(), name='roads-insert'),
    path('roads_view/insert2/', views.RoadsView.as_view(), name='roads-insert2'),
    path('roads_view/update/<int:id>/', views.RoadsView.as_view(), name='roads-update'),
    path('roads_view/delete/<int:id>/', views.RoadsView.as_view(), name='roads-delete'),
    
    # ViewSet URL-ji (REST framework)
    path('', include(router.urls)),
]


"""
REST API ENDPOINTS:

1. OSNOVNI ENDPOINTI
--------------------
GET  http://localhost:8000/roads/hello/
GET  http://localhost:8000/roads/logout/

2. ROADSVIEW (CUSTOM VIEW)
---------------------------
GET  http://localhost:8000/roads/roads_view/selectone/1/
GET  http://localhost:8000/roads/roads_view/selectall/
POST http://localhost:8000/roads/roads_view/insert/
POST http://localhost:8000/roads/roads_view/insert2/
POST http://localhost:8000/roads/roads_view/update/1/
POST http://localhost:8000/roads/roads_view/delete/1/

3. ROADSMODELVIEWSET (REST FRAMEWORK)
--------------------------------------
GET    http://localhost:8000/roads/roads/
GET    http://localhost:8000/roads/roads/1/
POST   http://localhost:8000/roads/roads/
PUT    http://localhost:8000/roads/roads/1/
PATCH  http://localhost:8000/roads/roads/1/
DELETE http://localhost:8000/roads/roads/1/
"""                            
