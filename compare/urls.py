from django.urls import path
from . import views

app_name = 'compare'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    # path('search/(?P<search>[\w-]+)/$', views.search, name='search'),
]
