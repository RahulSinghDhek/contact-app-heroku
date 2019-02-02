from django.conf.urls import url
from rest_framework.authtoken.views import obtain_auth_token
from .views import IndividualContact, ContactsList#, ContactsEmailSearch,ContactsNameSearch

urlpatterns = [
        url(r'^$',ContactsList.as_view(),name='list-contacts'),
        # url(r'^email/$',ContactsEmailSearch.as_view(),name='search-email-contacts'),
        # url(r'^name/$',ContactsNameSearch.as_view(),name='search-name-contacts'),
        url(r'^(?P<pk>[0-9]+)/?$',IndividualContact.as_view(),name='individual-contact'),
        url('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
