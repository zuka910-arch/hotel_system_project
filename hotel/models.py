from django.db import models


class HotelRoom(models.Model):
    
    ROOM_TYPES = [
        ('SGL', 'Single'),
        ('DBL', 'Double'),
        ('TWN', 'Twin'),
        ('SUI', 'Suite'),
    ]
    room_number = models.IntegerField(unique=True, verbose_name="Numero Camera")
    is_clean = models.BooleanField(default=True, verbose_name="Pulita")
    is_occupied = models.BooleanField(default=False, verbose_name="Occupata")

    room_type = models.CharField(max_length=3, choices=ROOM_TYPES, default='DBL', verbose_name="Tipo Camera")
    
    is_out_of_order = models.BooleanField(default=False, verbose_name="Fuori Servizio")
    
    notes = models.TextField(blank=True, null=True, verbose_name="Note")

    def __str__(self):
        return f"Camera {self.room_number} ({self.get_room_type_display()})"

class Ticket(models.Model):
    room = models.ForeignKey(HotelRoom, on_delete=models.CASCADE, related_name="tickets")
    informazione = models.TextField(verbose_name="Dettaglio")
    is_done = models.BooleanField(default=False, verbose_name="Completato")
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
    
    reply = models.TextField(blank=True, null=True, verbose_name="Risposta")

    def __str__(self):
        status = "✅ Fatto" if self.is_done else "❌ Da fare"
        return f"{status} - Camera {self.room.room_number}"
