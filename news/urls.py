from django.urls import path
from . import views

urlpatterns = [
    path('', views.Getlist.as_view(), name='list'),
    path('<int:pk>', views.Getdetail.as_view(), name='detail'),
    path('<int:pk>/delete', views.Getdelete.as_view(), name='delete'),
    path('create/', views.Getcreate.as_view(), name='create'),
    path('<int:pk>/update', views.Getupdate.as_view(), name='update'),
]