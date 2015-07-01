from rest_framework import serializers
from bassculture.models.item import Item
from bassculture.models.author import Author
from bassculture.models.source import Source

class ItemListSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Item
        fields = ('seller', 'url', 'source',)

class ItemDetailSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Item
        fields = ('url', 'seller', 'date', 'rism', 'pagination', 'dimensions', 'library', 'shelfmark',
            'item_notes', 'locations',)