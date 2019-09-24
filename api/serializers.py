from rest_framework import serializers

from .models import Metric


class MetricSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Metric
        fields = ['url', 'channel', 'country', 'os', 'impressions', 'clicks', 'installs', 'spend', 'revenue', 'date']
