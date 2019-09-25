from django.db.models import Sum, DecimalField
from django.db.models.functions import Cast
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
    queryset = Metric.objects.all().order_by('id')
    serializer_class = MetricSerializer
    filter_backends = (django_filters.DjangoFilterBackend, filters.OrderingFilter)
    filterset_class = MetricFilter
    ordering_fields = '__all__'

    def get_queryset(self):
        queryset = self.filter_queryset(self.queryset).values()
        group_by = self.request.query_params.get('groupby', None)
        annotated_fields = self.request.query_params.get('annotate', None)

        if not group_by:
            return queryset

        queryset = queryset.values(*group_by.split(','))

        if not annotated_fields:
            return queryset

        annotated_fields = annotated_fields.split(',')
        for field in annotated_fields:
            if field == 'cpi':
                queryset = queryset.annotate(cpi__sum=Cast(Sum('spend') / Sum('installs'), output_field=DecimalField()))
            else:
                queryset = queryset.annotate(Sum(field))

        return queryset
