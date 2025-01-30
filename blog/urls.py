from django.urls import path
from .import views

urlpatterns = [
    path('post/<int:id>/',views.post_detail,name='post_detail'),
    path('home/',views.index,name='home'),
    path('sidebar/',views.sidebar,name='sidebar'),
]
