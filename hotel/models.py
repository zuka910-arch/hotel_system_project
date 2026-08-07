from django.db import models



class HotelRoom(models.Model):
    room_number = models.IntegerField(unique=True, verbose_name="Numero Camera")
    is_clean = models.BooleanField(default=True, verbose_name="Pulita")
    is_occupied = models.BooleanField(default=False, verbose_name="Occupata")

    def __str__(self):
        return f"Camera {self.room_number}"

class Ticket(models.Model):
    # ForeignKey ნიშნავს, რომ ეს ტიკეტი კონკრეტულ ოთახზეა მიბმული
    room = models.ForeignKey(HotelRoom, on_delete=models.CASCADE, related_name="tickets")
    informazione = models.TextField(verbose_name="Dettaglio")
    is_done = models.BooleanField(default=False, verbose_name="Completato")
    
    # აქ პირდაპირ გვაქვს reply ველი, რომელიც შეიძლება თავიდან ცარიელი იყოს (blank=True)
    reply = models.TextField(blank=True, null=True, verbose_name="Risposta")

    def __str__(self):
        status = "✅ Fatto" if self.is_done else "❌ Da fare"
        return f"{status} - Camera {self.room.room_number}"
# Create your models here.
