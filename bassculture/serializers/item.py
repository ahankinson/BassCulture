from rest_framework import serializers
from bassculture.models.author import Author
from bassculture.models.source import Source
from bassculture.models.item import Item


class ItemListSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Item
        fields = ('seller', 'url', 'source_title', 'author_name',
                  'source_date', 'source_edition', 'publisher',)


class ItemDetailSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Item
        fields = ('url', 'seller', 'pagination', 'dimensions', 'library',
                  'shelfmark', 'item_notes', 'source_edition', 'source_date',
                  'item_notes', 'source_title', 'source_printer',
                  'source_publisher', 'source_author', 'source_rism',
                  'source_orientation', 'source_gore',)
