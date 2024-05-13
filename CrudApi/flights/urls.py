from django.urls import path
from . import views
urlpatterns = [  
    path('',views.create),
    path('search/',views.search),
    path('update/',views.update),
    path('delete/',views.delete),

]