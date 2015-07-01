from rest_framework import serializers
from bassculture.models.source import Source
from bassculture.models.author import Author

class SourceListSerializer(serializers.HyperlinkedModelSerializer):
    short_title = serializers.ReadOnlyField()

    class Meta:
        model = Source
        fields = ('short_title', 'authors', 'date', 'rism', 'locations',)

class SourceDetailSerializer(serializers.HyperlinkedModelSerializer):
    full_title = serializers.ReadOnlyField()
    short_title = serializers.ReadOnlyField()

    class Meta:
        model = Source