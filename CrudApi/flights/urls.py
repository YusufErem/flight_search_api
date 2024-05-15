from django.urls import path
from . import views
urlpatterns = [  
    path('',views.create),
    path('search_flight/',views.search_flight),
    path('search_airport/',views.search_airport),
    path('update/',views.update),
    path('delete/',views.delete),

]