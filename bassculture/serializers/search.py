import os
from rest_framework import serializers

class SearchSerializer(serializers.Serializer):
    url = serializers.SerializerMethodField("record_url")
    title = serializers.ReadOnlyField()
    content_type = serializers.ReadOnlyField()
    source_title = serializers.ReadOnlyField()

    def record_url(self, obj, *args, **kwargs):
        request = self.context.get('request', None)
        type = obj.model_name.lower()
        pk = obj.pk
        # This should always be relative to the root, not the current path.
        return request.build_absolute_uri(os.path.join('/', type, pk))
