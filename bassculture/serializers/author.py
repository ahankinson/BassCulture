from rest_framework import serializers
from bassculture.models.author import Author
from bassculture.models.source import Source


class AuthorListSerializer(serializers.HyperlinkedModelSerializer):
    name = serializers.ReadOnlyField()

    class Meta:
        model = Author


class AuthorSourceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Source
        fields = ('short_title', 'url', 'date', 'edition',)


class AuthorDetailSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField()
    sources = AuthorSourceSerializer(many=True)

    class Meta:
        model = Author
        fields = ('biographical_info', 'author', 'sources',)
