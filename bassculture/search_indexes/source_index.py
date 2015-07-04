from haystack import indexes
from bassculture.models.source import Source


class SourceIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr="short_title")
    short_title = indexes.CharField(model_attr="short_title", faceted=True)
    author = indexes.CharField(model_attr="author__name", faceted=True)
    description = indexes.CharField(model_attr="description")
    publisher = indexes.CharField(model_attr="publisher")

    def get_model(self):
        return Source

    # def prepare_item_library(self, obj):
    #     return '' if not obj.item else obj.item.library