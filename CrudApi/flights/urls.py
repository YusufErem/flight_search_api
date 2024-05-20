from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('ucuslar',views.UcuslarViewset, basename="ucuslar")
router.register('airport',views.HavaalaniViewset,basename="airport")






urlpatterns = [  
    path('',include(router.urls))
]