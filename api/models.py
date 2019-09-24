from django.db import models


# Create your models here.
class Metric(models.Model):
    channel = models.CharField(max_length=50)
    country = models.CharField(max_length=2)
    os = models.CharField(max_length=10)
    impressions = models.IntegerField()
    clicks = models.IntegerField()
    installs = models.IntegerField()
    spend = models.DecimalField(max_digits=10, decimal_places=2)
    revenue = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    @classmethod
    def upload_data(cls, filename='dataset.csv'):
        import csv
        import decimal
        with open(filename) as f:
            reader = csv.reader(f)
            next(reader, None)  # skip the header
            for row in reader:
                cls.objects.create(channel=row[1],
                                   country=row[2],
                                   os=row[3],
                                   impressions=int(row[4]),
                                   clicks=int(row[5]),
                                   installs=int(row[6]),
                                   spend=decimal.Decimal(row[7]),
                                   revenue=decimal.Decimal(row[8]),
                                   date=row[0])
