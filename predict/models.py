from django.db import models

FURNISHED_CHOICES = (
    ('no', 'no'),
    ('yes', 'yes'),
)

class PredResults(models.Model):

    bedrooms=models.FloatField()	
    bathrooms=models.FloatField() 
    land_size=models.FloatField()
    furnished=models.CharField(max_length=5, choices=FURNISHED_CHOICES)
    province=models.CharField(max_length=50)	
    district=models.CharField(max_length=50)	
    sector=models.CharField(max_length=50)
    prediction=models.FloatField()

    def __str__(self):
        return self.prediction
    
class PredResultSales(models.Model):

    property_type=models.CharField(max_length=50)	
    bedrooms=models.FloatField()	
    bathrooms=models.FloatField() 
    province=models.CharField(max_length=50)	
    district=models.CharField(max_length=50)	
    sector=models.CharField(max_length=50)
    area=models.FloatField()
    prediction=models.FloatField()

    def __str__(self):
        return self.prediction
