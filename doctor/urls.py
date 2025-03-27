from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
router = DefaultRouter()

router.register('list', views.DoctorViewset)#antenna
router.register('specialization', views.SpecializationViewset)#antenna
router.register('available_time', views.AvailableTimeViewset)#antenna
router.register('designation', views.DesignationViewset)#antenna
router.register('reviews', views.ReviewViewset)#antenna


urlpatterns = [
    path('', include(router.urls)),
]