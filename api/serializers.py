from rest_framework import serializers

from .models import Metric


class MetricSerializer(serializers.HyperlinkedModelSerializer):
    cpi = serializers.SerializerMethodField()

    def get_cpi(self, obj):
        return obj.spend / obj.installs

    def to_representation(self, instance):
        """
        Function for working with an instance represented by a dictionary, not by a model object.
        """
        return instance

    class Meta:
        model = Metric
        fields = '__all__'
