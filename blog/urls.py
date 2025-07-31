from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.detail),
    path('', views.index),
]




'''

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:pk>/', views.detail)
]
'''