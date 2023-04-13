from django.urls import path
from . import views

app_name = 'typingtest'

urlpatterns = [
    path('', views.index, name='index'),
    path('start/', views.start, name='start'),
    # path('typing/', views.typing, name='typing'),
    path('results/', views.results, name='results')
]
