from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from snippets.views import *
from rest_framework import renderers


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', SnippetViewSet)
router.register(r'users', UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
#
# snippet_list = SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# snippet_detail = SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# snippet_highlight = SnippetViewSet.as_view({
#     'get': 'highlight'
# }, renderer_classes=[renderers.StaticHTMLRenderer])
# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })
#
# urlpatterns = [
#     path('', api_root),
#     #  Вариант 6
#     path('snippets/',snippet_list, name='snippet-list'),
#     path('snippets/<pk>/', snippet_detail, name='snippet-detail'),
#     path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
#     path('users/', user_list, name='user-list'),
#     path('users/<int:pk>/', user_detail, name='user-detail'),
#
#     #  Вариант 5
#     # path('snippets/', SnippetList.as_view(), name='snippet-list'),
#     # path('snippets/<pk>/', SnippetDetail.as_view(), name='snippet-detail'),
#     # path('snippets/<int:pk>/highlight/', SnippetHighlight.as_view(), name='snippet-highlight'),
#     # path('users/', UserList.as_view(), name='user-list'),
#     # path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
#
#     #  Вариант 1\2
#     # path('snippets/', snippet_list, name='no_pk_views'),
#     # path('snippets/<pk>/', snippet_detail, name='pk_views')
# ]
#
# urlpatterns = format_suffix_patterns(urlpatterns)
