from django.urls import path
from . import views
from .views import GeeksList, detail_view, update_view, delete_view, MyView, GeeksCreate
# importing views from views..py
# from .views import geeks_view

from .views import GeeksUpdateView

urlpatterns = [
	path('geeks/', views.geeks_view),
    # path('room/', views.room, name="room"),
    path('home/', views.home_view, name="home"),
    path('list/', views.list_view),
    path('create/', views.create_view),
    path('list_view/', GeeksList.as_view()),
    path('<id>', detail_view ),
    path('<id>/update/', update_view),
    path('<id>/delete/', delete_view ),
    path('about/', MyView.as_view()),
    path('geekscreate/', GeeksCreate.as_view() ),
    path('<pk>/update', GeeksUpdateView.as_view()),
]


