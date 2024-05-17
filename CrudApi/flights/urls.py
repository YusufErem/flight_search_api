from django.urls import path
from . import views
urlpatterns = [  
    path('flight_create',views.flight_create),
    path('airport_create',views.airport_create),
    path('search_flight/',views.search_flight),
    path('search_airport/',views.search_airport),
    path('update/',views.update),
    path('delete/',views.delete),

]