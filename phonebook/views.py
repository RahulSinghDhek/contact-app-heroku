from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from .serializers import ContactSerializer
from .models import Contact
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from.filters import CustomSearchFilter
#from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import CursorPagination

# class ContactsNameSearch(ListAPIView):
#     queryset = Contact.objects.all()
#     serializer_class = ContactSerializer
#     filter_backends = (DjangoFilterBackend,CustomSearchFilter,)
#     search_fields = ('contact_name')
#     filter_fields = ('contact_name')
#
# class ContactsEmailSearch(ListAPIView):
#     queryset = Contact.objects.all()
#     serializer_class = ContactSerializer
#     filter_backends = (DjangoFilterBackend,CustomSearchFilter,)
#     search_fields = ('email')
#     filter_fields = ('email')


class ContactsList(ListCreateAPIView):
    #permission_classes = (IsAuthenticated,)
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    filter_backends = (DjangoFilterBackend,CustomSearchFilter)
    search_fields = ('contact_name', 'email')
    filter_fields = ('contact_name', 'email')



class IndividualContact(RetrieveUpdateDestroyAPIView):
    #permission_classes = (IsAuthenticated,)
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


