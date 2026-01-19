from django.urls import path, include
from . import views
from rest_framework import routers

# ====================================
# ROUTER ZA REST API
# ====================================
router = routers.DefaultRouter()
router.register(r'parcels', views.ParcelsModelViewSet)
router.register(r'parcelsowners', views.ParcelOwnersModelViewSet)

urlpatterns = [
    # ====================================
    # KEYCLOAK OIDC - HELLO WORLD TEST
    # ====================================
    path("hello_world/", views.hello_world, name="hello_world"),

    # ====================================
    # PARCELS VIEW - SELECTONE
    # ====================================
    path('parcels_view/selectone/<int:id>/', views.ParcelsView.as_view(), name='parcels_selectone'),
    
    # ====================================
    # PARCELS VIEW - SELECTALL
    # ====================================
    path('parcels_view/selectall/', views.ParcelsView.as_view(), name='parcels_selectall'),
    
    # ====================================
    # PARCELS VIEW - INSERT
    # ====================================
    path('parcels_view/insert/', views.ParcelsView.as_view(), name='parcels_insert'),
    
    # ====================================
    # PARCELS VIEW - INSERT2 (alternative method)
    # ====================================
    path('parcels_view/insert2/', views.ParcelsView.as_view(), name='parcels_insert2'),
    
    # ====================================
    # PARCELS VIEW - UPDATE
    # ====================================
    path('parcels_view/update/<int:id>/', views.ParcelsView.as_view(), name='parcels_update'),
    
    # ====================================
    # PARCELS VIEW - DELETE
    # ====================================
    path('parcels_view/delete/<int:id>/', views.ParcelsView.as_view(), name='parcels_delete'),
    
    # ====================================
    # REST API ROUTER (DRF ViewSets)  (REST framework)
    # ====================================
    path('', include(router.urls)),
    
    # ====================================
    # LOGOUT - Keycloak
    # ====================================
    path('logout/', views.logout_view, name='logout'),
]

"""
REST API ENDPOINTS:

1. OSNOVNI ENDPOINTI
--------------------
GET  http://localhost:8000/parcels/hello/
GET  http://localhost:8000/parcels/logout/

2. PARCELSVIEW (CUSTOM VIEW)
-----------------------------
GET  http://localhost:8000/parcels/parcels_view/selectone/1/
GET  http://localhost:8000/parcels/parcels_view/selectall/
POST http://localhost:8000/parcels/parcels_view/insert/
POST http://localhost:8000/parcels/parcels_view/insert2/
POST http://localhost:8000/parcels/parcels_view/update/1/
POST http://localhost:8000/parcels/parcels_view/delete/1/

3. PARCELSMODELVIEWSET (REST FRAMEWORK)
----------------------------------------
GET    http://localhost:8000/parcels/parcels/
GET    http://localhost:8000/parcels/parcels/1/
POST   http://localhost:8000/parcels/parcels/
PUT    http://localhost:8000/parcels/parcels/1/
PATCH  http://localhost:8000/parcels/parcels/1/
DELETE http://localhost:8000/parcels/parcels/1/
"""

