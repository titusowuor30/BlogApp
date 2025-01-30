from django.urls import path
from .import views

urlpatterns = [
    path('',views.post_detail,name='post_detail'),
    path('index/',views.index,name='index'),
    path('sidebar/',views.sidebar,name='sidebar'),
]
