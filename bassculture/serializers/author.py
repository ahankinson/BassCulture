from rest_framework import serializers
from bassculture.models.author import Author
from bassculture.models.source import Source


class AuthorListSerializer(serializers.HyperlinkedModelSerializer):
    full_name = serializers.ReadOnlyField()

    class Meta:
        model = Author


class AuthorSourceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Source
        fields = ('url', 'short_title',)


class AuthorDetailSerializer(serializers.HyperlinkedModelSerializer):
    full_name = serializers.ReadOnlyField()
    short_title = AuthorSourceSerializer(many=True)

    class Meta:
        model = Author
        fields = ('short_title', 'full_name',)
