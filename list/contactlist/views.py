# -*- coding: utf-8 -*-
from rest_framework import generics
from django.shortcuts import render
from contactlist.models import(Contact)
from contactlist.serializers import(ContactSerializers, ContactBasicSerializers)


class ContactList(generics.ListCreateAPIView):
   
    queryset = Contact.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ContactSerializers
        else:
            return ContactBasicSerializers


# class ContactView(generics.ListCreateAPIView):
#     serializer_class = ContactSerializers
#     queryset = Contact.objects.all()


class ContactDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ContactSerializers
    queryset = Contact.objects.filter()


def index(request,):
    #all_contact = Contact.objects.all()
    return render(request, 'list.html',)


