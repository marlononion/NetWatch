from django.db import models

# Create your models here.
from django.db import models

class NetworkTraffic(models.Model):
    avg_packet_size = models.FloatField()
    total_packets = models.IntegerField()
    # outros campos relevantes
