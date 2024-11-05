from django.contrib import admin

from flights.models import Customer, Havaalanlari, Ucuslar

# Register your models here.
admin.site.register(Havaalanlari)
admin.site.register(Ucuslar)
admin.site.register(Customer)