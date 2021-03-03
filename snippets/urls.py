from django.urls import path
from snippets.views import *

urlpatterns = [
    path('snippets/', snippet_list, name='no_pk_views'),
    path('snippets/<pk>/', snippet_detail, name='pk_views')
]
