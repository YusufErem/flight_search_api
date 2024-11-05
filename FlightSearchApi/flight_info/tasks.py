from celery import shared_task
from .models import Ucuslar, Havaalanlari
from datetime import datetime, timedelta
import random

@shared_task
def create_flight_info():
    havaalanlari = list(Havaalanlari.objects.all())
    if len(havaalanlari) < 2:
        print("Yeterli havaalanı yok.")
        return

    for _ in range(10):  # Her gün 10 uçuş bilgisi oluştur
        kalkis_havaalani = random.choice(havaalanlari)
        varis_havaalani = random.choice(havaalanlari)
        
        while varis_havaalani == kalkis_havaalani:
            varis_havaalani = random.choice(havaalanlari)
        
        kalkis_zamani = datetime.now() + timedelta(days=random.randint(1, 30))
        inis_zamani = kalkis_zamani + timedelta(hours=random.randint(1, 12))
        
        Ucuslar.objects.create(
            kalkis_havaalani=kalkis_havaalani,
            varis_havaalani=varis_havaalani,
            kalkis_zamani=kalkis_zamani,
            inis_zamani=inis_zamani,
            fiyat=random.uniform(100, 1000)
        )

    print("10 uçuş bilgisi başarıyla oluşturuldu.")