# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from Serializers import *
from models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status


# Create your views here.
#url without primary key
#url with a primary key
#need at least 2 views
    #one with a get and post, this gets all (no need for primary key reference)
    # another with a get, put and delete

class BookCreateAllView(APIView):

    def get(self, request, *args, **kwargs):
        BookPick = Books.objects.all() #ref book model, uses manager for that model
        # and calls function within
        #going into a model, going to manager, telling it to get all the objects
        BooksPicks = BooksSerializer(BookPick, many=True) #passing model ref to book seriializer, instance/row of database
        # make sure to inclue many=True since we're passing more than 1
        return Response(BooksPicks.data) #return the JSON


    def post(self, request, *args, **kwargs):
        data = BooksSerializer(data = request.data) #grabbing data that came in and checking validity
        if data.is_valid(raise_exception=True):
            validdata=data.validateData
            type = BooksSerializer(validdata)
            type.save() #if data is valid save it else reject it
            createdtype = BooksSerializer(type)
            return Response(createdtype.data)


class BookView2NotSure(APIView): #recommended
    #get and post in first view doesn't require key words in the url
    # in this view it does because we need to pass an actual reference to it

    def get(self, request, *args, **kwargs):
        instance = kwargs.get('pk', 0)
        instance = get_object_or_404(Books, pk=instance)
        instance=BooksSerializer(instance)
        return Response(instance.data)


    def put(self, request, *args, **kwargs):
        instance = kwargs.get('pk',0)
        instance = get_object_or_404(Books, pk=instance)
        serializeddata=BooksSerializer(instance, data=request.data, partial=True) #checks validity of data sent,
        # then takes db object and applies new info to object,
        # updates old db object with new one and then saves it
        if serializeddata.is_valid(raise_exception=True): #check if data is valid and save it
            serializeddata.save()
            return Response(serializeddata.data)


    def delete(self, request, *args, **kwargs):
        instance = kwargs.get('pk', 0)
        instance = get_object_or_404(Books, pk=instance)
        instance.delete()
        return Response(status=status.HTTP_200_OK)
    #primary key comes in to URL and find object that has this primary key ref
    #loads it( get or 404) once it has reference then delete it and p[ythojn does it by reference
    #return status of 200 - traditional code for it all worked