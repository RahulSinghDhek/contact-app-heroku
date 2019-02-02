from .models import Contact
import django_filters
from rest_framework.filters import SearchFilter

class CustomSearchFilter(SearchFilter):
    def __init__(self,prefix="search_"):
        self.search_field_prefix = prefix

    def get_search_terms(self, request):
        search_fields = getattr(request.resolver_match.func.view_class, 'search_fields', list())
        params = []

        for query_param in request.query_params:
            # check if query paramater is a search paramater
            if query_param.startswith(self.search_field_prefix):
                field = self.search_field_prefix.join(
                    query_param.split(self.search_field_prefix)[1:]
                )

                # only apply search filter for fields that are in the views search_fields
                if field in search_fields:
                    params.append(request.query_params.get(query_param, ''))

        return params
