from rest_framework import serializers
from bassculture.models.source import Source
from bassculture.models.author import Author
from bassculture.models.item import Item


class SourceListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Source


class SourceAuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author


class SourceItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item


class SourceDetailSerializer(serializers.HyperlinkedModelSerializer):
    author = SourceAuthorSerializer()
    items = SourceItemSerializer(many=True)

    class Meta:
        model = Source
