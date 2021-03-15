from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from snippets.views import *

urlpatterns = [
    path('snippets/', SnippetList.as_view(), name='snippet-list'),
    path('snippets/<pk>/', SnippetDetail.as_view(), name='pk_views'),
    path('snippets/<int:pk>/highlight/', SnippetHighlight.as_view()),
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('', api_root),
    # path('snippets/', snippet_list, name='no_pk_views'),
    # path('snippets/<pk>/', snippet_detail, name='pk_views')
]

urlpatterns = format_suffix_patterns(urlpatterns)
