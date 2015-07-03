from rest_framework import serializers
from bassculture.models.author import Author
from bassculture.models.source import Source


class AuthorListSerializer(serializers.HyperlinkedModelSerializer):
    full_name = serializers.ReadOnlyField()

    class Meta:
        model = Author

class AuthorDetailSerializer(serializers.HyperlinkedModelSerializer):
    name = serializers.ReadOnlyField()

    class Meta:
        model = Author
        fields = ('biographical_info', 'name',)
