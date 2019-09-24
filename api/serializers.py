from rest_framework import serializers

from .models import Metric


class MetricSerializer(serializers.HyperlinkedModelSerializer):
    cpi = serializers.SerializerMethodField()

    def get_cpi(self, obj):
        return round(obj.spend / obj.installs, 2)

    class Meta:
        model = Metric
        fields = '__all__'
