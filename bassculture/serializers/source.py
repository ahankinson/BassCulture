from rest_framework import serializers
from bassculture.models.source import Source
from bassculture.models.author import Author

class SourceListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Source

class SourceAuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author

class SourceDetailSerializer(serializers.HyperlinkedModelSerializer):
    author = SourceAuthorSerializer()

    class Meta:
        model = Source