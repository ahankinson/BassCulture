from rest_framework import serializers
from bassculture.models.tune import Tune


class TuneListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tune


class TuneDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tune