from rest_framework import serializers
# from bassculture.models.author import Author
# from bassculture.models.source import Source
from bassculture.models.item import Item
from bassculture.models.tune import Tune


class ItemTunesSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Tune


class ItemListSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Item
        fields = ('seller', 'url', 'source_title',
                  'source_date', 'source_edition', 'source_author',)


class ItemDetailSerializer(serializers.HyperlinkedModelSerializer):
    tunes = ItemTunesSerializer(many=True)

    class Meta:
        model = Item
        fields = ('url', 'seller', 'pagination', 'dimensions', 'library',
                  'shelfmark', 'item_notes', 'source_edition', 'source_date',
                  'item_notes', 'source_title', 'source_printer',
                  'source_publisher', 'source_author', 'source_rism',
                  'source_orientation', 'source_gore', 'id', 'tunes',
                  'source_description', 'source_locations',
                  'item_biographicalinfo', 'item_authorid',)
