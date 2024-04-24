from django.urls import path
from . import views

urlpatterns = [
    path('', views.dance_home, name='home'),
    path('', views.dance_list),
    path('', views.index, name='home'),
    path('add', views.add, name='add'),
    path('<int:pk>', views.ArtistDetailView.as_view(), name='detail'),
    path('<int:pk>/update', views.ArtistUpdateView.as_view(), name='update')
]