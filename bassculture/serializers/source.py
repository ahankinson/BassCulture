from rest_framework import serializers
from bassculture.models.source import Source
from bassculture.models.author import Author

class SourceListSerializer(serializers.HyperlinkedModelSerializer):
    short_title = serializers.ReadOnlyField()

    class Meta:
        model = Source

class SourceAuthorSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Author

class SourceDetailSerializer(serializers.HyperlinkedModelSerializer):
    authors = SourceAuthorSerializer(many=True)
    full_title = serializers.ReadOnlyField()
    short_title = serializers.ReadOnlyField()

    class Meta:
        model = Source