from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=200, null=False)
    image = models.CharField(max_length=500, null=False)
    seria = models.CharField(max_length=100, null=False)
    screen_type = models.CharField(max_length=100, null=False)
    video_card = models.CharField(max_length=200, null=False)
    ssd_amount = models.CharField(max_length=100)
    hdd_amount = models.CharField(max_length=100)
    processor = models.CharField(max_length=300, null=False)
    ram_amount = models.CharField(max_length=100, null=False)
    color = models.CharField(max_length=100, null=False)
    country = models.CharField(max_length=100, null=False)