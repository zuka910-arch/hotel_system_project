from django.shortcuts import render
from .models import HotelRoom

def dashboard(request):
    rooms = HotelRoom.objects.all()
    # აქ დაემატა 'pages/' 👇
    return render(request, 'pages/dashboard.html', {'rooms': rooms})