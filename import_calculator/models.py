from django.db import models

# CONSTANTS
CHARFIELD_MAX_LEN = 256


# Create your models here.
class Type(models.Model):
    """
    In-Game entity that is marketable
    """
    type_id = models.IntegerField(unique=True)
    type_name = models.CharField(max_length=CHARFIELD_MAX_LEN)
    type_vol = models.CharField(max_length=CHARFIELD_MAX_LEN)


class Region(models.Model):
    """
    In-Game region
    """
    region_id = models.IntegerField(unique=True)
    region_name = models.CharField(max_length=CHARFIELD_MAX_LEN)


class Structure(models.Model):
    """
    In-Game player built structure
    """
    structure_id = models.IntegerField(unique=True)
    structure_name = models.CharField(max_length=CHARFIELD_MAX_LEN)
    owner_id = models.IntegerField()  # Corporation ID
    solar_system_id = models.IntegerField()
    type_id = models.IntegerField()  # Type of structure


class RegionMarketHistory(models.Model):
    """
    Market history of an entity in a region
    """
    type_id = models.ForeignKey('Type', on_delete=models.CASCADE)
    region_id = models.ForeignKey('Structure', on_delete=models.CASCADE)
    average = models.FloatField()  # Average Price
    date = models.DateField()  # The date of this historical statistic entry
    highest = models.FloatField()  # Highest Price
    lowest = models.FloatField()  # Lowest Price
    order_count = models.IntegerField()  # Total number of orders happened that day
    volume = models.IntegerField()  # Total volume moved


class StructureMarketData(models.Model):
    """
    Market data of an entity in a structure/station
    """
    type_id = models.ForeignKey('Type', to_field='type_id', on_delete=models.CASCADE)
    structure_id = models.ForeignKey('Structure', to_field='structure_id', on_delete=models.CASCADE)
    average = models.FloatField()  # Average Price
    highest = models.FloatField()  # Highest Price
    lowest = models.FloatField()  # Lowest Price
    sell_volume = models.IntegerField()  # Total volume of entity as sell orders
    buy_volume = models.IntegerField()  # Total volume of entity as buy orders
