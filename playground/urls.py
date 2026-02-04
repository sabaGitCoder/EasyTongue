from django.urls import path
from . import  views
 
urlpatterns = [
  path('wellcome/',views.wellcome)
]