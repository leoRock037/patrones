from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView )

from kpiApp.models import *
from api.serializers import OrgSerializer


@api_view(['GET', 'POST'])
def org_lista(request):
    # GET Request
    if request.method == 'GET':
        org = Organizacion.objects.all()
        serializer = OrgSerializer(org)
        return Response(serializer.data)

    # POST Request
    if request.method == 'POST':
        serializer = OrgSerializer(data=request.DATA)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )



