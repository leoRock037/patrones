from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView )

from kpiApp.models import Kpi
from api.serializers import KpiSerializer


@api_view(['GET', 'POST'])
def kpi_lista(request):
    # GET Request
    if request.method == 'GET':
        kpi = Kpi.objects.all()
        serializer = KpiSerializer(kpi)
        return Response(serializer.data)

    # POST Request
    if request.method == 'POST':
        serializer = KpiSerializer(data=request.DATA)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )



