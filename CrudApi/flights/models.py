from django.db import models

# Create your models here.

class Havaalanlari(models.Model):
    sehir = models.CharField()

class Ucuslar(models.Model):
    kalkis_havaalani = models.ForeignKey(Havaalanlari,max_length=100, on_delete= models.CASCADE,related_name = 'kalkis_havaalanlari')
    varis_havaalani = models.ForeignKey(Havaalanlari,max_length=100, on_delete = models.CASCADE, related_name = 'varis_havaalanlari')
    kalkis_zamani = models.DateTimeField()
    donus_zamani = models.DateTimeField()
    fiyat = models.DecimalField(max_digits=10, decimal_places=2)