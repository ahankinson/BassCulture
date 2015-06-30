from rest_framework import serializers
from bassculture.models.source import Source
from bassculture.models.author import Author
from bassculture.models.publisher import Publisher
from bassculture.models.printer import Printer


class SourceListSerializer(serializers.HyperlinkedModelSerializer):
    short_title = serializers.ReadOnlyField()

    class Meta:
        model = Source

class SourceAuthorSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Author

class SourcePublisherSerializer(serializers.HyperlinkedModelSerializer):
    name = serializers.ReadOnlyField()

    class Meta:
        model = Publisher
        fields = ('name',)

class SourcePrinterSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Printer

class SourceDetailSerializer(serializers.HyperlinkedModelSerializer):
    authors = SourceAuthorSerializer(many=True)
    full_title = serializers.ReadOnlyField()
    publisher = SourcePublisherSerializer()
    printer = SourcePrinterSerializer()

    class Meta:
        model = Source
