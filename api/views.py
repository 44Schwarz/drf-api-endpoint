from rest_framework import viewsets, filters
from django_filters import rest_framework as django_filters

from .models import Metric
from .serializers import MetricSerializer


class MetricFilter(django_filters.FilterSet):
    date = django_filters.DateFromToRangeFilter()
    channel = django_filters.CharFilter()
    country = django_filters.CharFilter()
    os = django_filters.CharFilter()

    class Meta:
        model = Metric
        fields = ['date', 'channel', 'country', 'os']


# Create your views here.
class MetricViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows metrics to be viewed.
    """
    queryset = Metric.objects.all()
    serializer_class = MetricSerializer
    filter_backends = (django_filters.DjangoFilterBackend, filters.OrderingFilter)
    filterset_class = MetricFilter
    ordering_fields = ('channel', 'country', 'os', 'impressions', 'clicks',
                       'installs', 'spend', 'revenue', 'date', 'cpi')
