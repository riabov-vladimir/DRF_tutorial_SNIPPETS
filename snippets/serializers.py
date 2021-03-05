from django.contrib.auth.models import User
from rest_framework import serializers
from snippets.models import *


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']
        extra_kwargs = {'code': {'required': False}}


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True,
                                                  queryset=Snippet.objects.all())
    # поле snippets это обратная связь и она не включается по умолчанию в классе Мета

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']


"""
    Первый вариант: используем класс Serializer
    Суть его отличия от класса ModelSerializer такая же, как в случае
    Form и ModelForm. Первый вариант более громоздкий, но более гибкий
    в настройке. 
"""
#
# class SnippetSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(
#         required=False,
#         allow_blank=True,
#         max_length=100
#     )
#     code = serializers.CharField(
#         style={'base_template': 'textarea.html'},
#         required=False
#     )
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
#
#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Snippet.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance
#
