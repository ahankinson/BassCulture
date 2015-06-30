from rest_framework import serializers
from bassculture.models.item import Item
from bassculture.models.author import Author
from bassculture.models.publisher import Publisher
from bassculture.models.printer import Printer


class ItemPrinterSerializer(serializers.HyperlinkedModelSerializer):
    name = serializers.ReadOnlyField()

    class Meta:
        model = Printer
        fields = ('name',)

class ItemListSerializer(serializers.HyperlinkedModelSerializer):
   
    class Meta:
        model = Item
        fields = ('seller', 'url',)


class ItemDetailSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Item
        fields = ('url', 'seller', 'date', 'rism', 'pagination', 'dimensions', 'library', 'shelfmark',
            'item_notes', 'library', 'gore', 'orientation', 'locations',)
