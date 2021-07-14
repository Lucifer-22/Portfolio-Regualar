from django.urls import path


from . import views
from .views import index, bio_view, getUserInfo

urlpatterns = [
    path('', views.index, name='index'),
    path('api/<str:username>',views.bio_view, name='bio_view'),
    path('user', views.getUserInfo, name='getUserInfo'),
   # path('mysite/', HomePageView.as_view(), name='home'),
]