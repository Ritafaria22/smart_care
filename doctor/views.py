from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.permissions import BasePermission
from rest_framework import filters, pagination


# Create your views here.
class SpecializationViewset(viewsets.ModelViewSet):
       queryset = models.Specialization.objects.all()
       serializer_class = serializers.SpecializationSerializer

class AvailableTimeForSpecificDoctor(filters.BaseFilterBackend):
       def filter_queryset(self, request, query_set, view):
              doctor_id = request.query_params.get("doctor_id")
              if doctor_id:
                     return query_set.filter(doctor = doctor_id)
              return query_set

class AvailableTimeViewset(viewsets.ModelViewSet):
       permission_classes = [IsAuthenticatedOrReadOnly]
       queryset = models.AvailableTime.objects.all()
       serializer_class = serializers.AvailableTimeSerializer
       filter_backends = [AvailableTimeForSpecificDoctor]


class DesignationViewset(viewsets.ModelViewSet):
       queryset = models.Designation.objects.all()
       serializer_class = serializers.DesignationSerializer

class ReviewViewset(viewsets.ModelViewSet):
       queryset = models.Review.objects.all()
       serializer_class = serializers.ReviewSerializer


class DoctorPagination(pagination.PageNumberPagination):
       page_size = 1 #item per page
       page_size_query_param = page_size
       max_page_size = 100



class DoctorViewset(viewsets.ModelViewSet):
       queryset = models.Doctor.objects.all()
       serializer_class = serializers.DoctorSerializer
       pagination_class = DoctorPagination


  
