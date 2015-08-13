import os
from rest_framework import serializers


class SearchSerializer(serializers.Serializer):
    url = serializers.SerializerMethodField("record_url")
    title = serializers.ReadOnlyField()
    content_type = serializers.ReadOnlyField()
    source_title = serializers.ReadOnlyField()
    alternate_spellings = serializers.ReadOnlyField()
    source_date = serializers.ReadOnlyField()
    source_edition = serializers.ReadOnlyField()
    author_surname = serializers.ReadOnlyField()

    def record_url(self, obj, *args, **kwargs):
        request = self.context.get('request', None)
        # type = obj.model_name.lower() this returns a 'AttributeError: 'dict' object has no attribute 'model_name'' error
        type = self.__class__.__name__.lower()
        # pk = obj.pk this returns a 'AttributeError: 'dict' object has no attribute 'pk'' error
        # This should always be relative to the root, not the current path.
        return request.build_absolute_uri(os.path.join('/', type,))
