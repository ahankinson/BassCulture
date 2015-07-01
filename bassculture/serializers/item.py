from rest_framework import serializers
from bassculture.models.item import Item
from bassculture.models.author import Author
from bassculture.models.source import Source

class ItemListSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Item
        fields = ('seller', 'url', 'source_title', 'author_name',)

class ItemDetailSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Item
        fields = ('url', 'seller', 'pagination', 'dimensions', 'library', 'shelfmark',
            'item_notes',)