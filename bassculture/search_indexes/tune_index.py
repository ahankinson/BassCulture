from haystack import indexes
from bassculture.models.tune import Tune


class TuneIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr="name")
    alternate_spellings = indexes.CharField(model_attr="alternate_spellings", null=True)
    source_title = indexes.CharField(model_attr="item__source__short_title", faceted=True)
    source_date = indexes.CharField(model_attr="item__source__date")
    source_edition = indexes.CharField(model_attr="item__source__edition")
    full_source_title = indexes.CharField(model_attr="item__source__full_title")
    author = indexes.CharField(model_attr="item__source__author__name", faceted=True)
    item_library = indexes.CharField(model_attr="item__library")

    def get_model(self):
        return Tune
