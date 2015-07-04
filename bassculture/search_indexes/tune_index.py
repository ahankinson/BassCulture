from haystack import indexes
from bassculture.models.tune import Tune


class TuneIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr="name")
    source_title = indexes.CharField(model_attr="item__source__short_title", faceted=True)
    author = indexes.CharField(model_attr="item__source__author__name", faceted=True)
    item_library = indexes.CharField(model_attr="item__library")
    # author = indexes.CharField(model_attr="author")

    def get_model(self):
        return Tune
