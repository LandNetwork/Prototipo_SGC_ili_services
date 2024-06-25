from django.urls import path, include
from rest_framework import routers
from ili_svc_app import views

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('get_file/<str:pk>/', view=views.get_file, name="export file xtf"),
    path('upload_file/', view=views.upload_file, name="upload file xtf")
]