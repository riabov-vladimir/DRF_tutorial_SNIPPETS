from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt  # bypasses csrf token validation
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


#        Вариант второй
#        - вводим объект Response, который умеет проверять типы
#        даных и работать с набором именованных кодов
#        - вводим декоратор отвечающий за методы запросов


@api_view(['GET', 'POST'])
def snippet_list(request):
    """
    Вью-функция отвечающая за отображение всех экземпляров класса Snippet
    и за создание новых экземпляров.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk):
    """
    Вью-функция отвечающая за отображение, удаление и обновление конкретного
    экземпляра класса Snippet с идентификатором равным PK.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#           Первый базовый вариант -- ВЬЮ-ФУНКЦИИ


# @csrf_exempt
# def snippet_list(request):
#     """
#     Вью-функция отвечающая за отображение всех экземпляров класса Snippet
#     и за создание новых экземпляров.
#     :param request:
#     :return:
#     """
#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#
#
# @csrf_exempt
# def snippet_detail(request, pk):
#     """
#
#     :param request:
#     :param pk:
#     :return:
#     """
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return JsonResponse(serializer.data)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(snippet, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#
#     elif request.method == 'DELETE':
#         snippet.delete()
#         return HttpResponse(status=204)
