from django.urls import path, include
from . import views
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'buildings', views.BuildingsModelViewSet) 
router.register(r'owners', views.OwnersModelViewSet)

urlpatterns = [
    # Pozdravna stran
    path('hello/', views.HelloWord.as_view(), name='hello'),
    
    # Logout
    path('logout/', views.custom_logout_view, name='logout'),
    
    # BuildingsView - CRUD operacije
    path('buildings_view/selectone/<int:id>/', views.BuildigsView.as_view(), name='buildings-selectone'),
    path('buildings_view/selectall/', views.BuildigsView.as_view(), name='buildings-selectall'),
    path('buildings_view/insert/', views.BuildigsView.as_view(), name='buildings-insert'),
    path('buildings_view/insert2/', views.BuildigsView.as_view(), name='buildings-insert2'),
    path('buildings_view/update/<int:id>/', views.BuildigsView.as_view(), name='buildings-update'),
    path('buildings_view/delete/<int:id>/', views.BuildigsView.as_view(), name='buildings-delete'),
    
    # ViewSet URL-ji (REST framework)
    path('', include(router.urls)),
]


"""
REST API ENDPOINTS:

1. OSNOVNI ENDPOINTI
--------------------
GET  http://localhost:8000/buildings/hello/
GET  http://localhost:8000/buildings/logout/

2. BUILDINGSVIEW (CUSTOM VIEW)
-------------------------------
GET  http://localhost:8000/buildings/buildings_view/selectone/1/
GET  http://localhost:8000/buildings/buildings_view/selectall/
POST http://localhost:8000/buildings/buildings_view/insert/
POST http://localhost:8000/buildings/buildings_view/insert2/
POST http://localhost:8000/buildings/buildings_view/update/1/
POST http://localhost:8000/buildings/buildings_view/delete/1/

3. BUILDINGSMODELVIEWSET (REST FRAMEWORK)
------------------------------------------
GET    http://localhost:8000/buildings/buildings/
GET    http://localhost:8000/buildings/buildings/1/
POST   http://localhost:8000/buildings/buildings/
PUT    http://localhost:8000/buildings/buildings/1/
PATCH  http://localhost:8000/buildings/buildings/1/
DELETE http://localhost:8000/buildings/buildings/1/
"""
