from django.contrib.auth.models import User
from rest_framework import serializers
from snippets.models import *


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    """
    The HyperlinkedModelSerializer has the following differences from ModelSerializer:

    It does not include the id field by default.
    It includes a url field, using HyperlinkedIdentityField.
    Relationships use HyperlinkedRelatedField, instead of PrimaryKeyRelatedField.

    """
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')


    class Meta:
        model = Snippet
        fields = ['url', 'id', 'highlight', 'owner', 'title', 'code', 'linenos', 'language', 'style']
        extra_kwargs = {'code': {'required': False}}


class UserSerializer(serializers.HyperlinkedModelSerializer):

    snippets = serializers.HyperlinkedIdentityField(
        many=True,
        view_name='snippet-detail',
        read_only=True
    )

    # поле snippets это обратная связь, поэтому как
    # поле она фактически не существует, её надо создавать

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']


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
