from rest_framework import serializers
from bassculture.models.item import Item
from bassculture.models.author import Author
from bassculture.models.publisher import Publisher
from bassculture.models.printer import Printer
from bassculture.models.source import Source


class ItemPrinterSerializer(serializers.HyperlinkedModelSerializer):
    name = serializers.ReadOnlyField()

    class Meta:
        model = Printer
        fields = ('name',)

class ItemTitleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Source

class ItemListSerializer(serializers.HyperlinkedModelSerializer):
    short_title = ItemTitleSerializer()

    class Meta:
        model = Item
        fields = ('seller', 'url', 'short_title',)

class ItemDetailSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Item
        fields = ('url', 'seller', 'date', 'rism', 'pagination', 'dimensions', 'library', 'shelfmark',
            'item_notes', 'locations',)