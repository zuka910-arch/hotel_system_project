from django.shortcuts import render, redirect, get_object_or_404
from .models import HotelRoom

def dashboard(request):
    rooms = HotelRoom.objects.all()
    return render(request, 'pages/dashboard.html', {'rooms': rooms})


def toggle_clean_status(request, room_id):
    if request.method == 'POST':
        room = get_object_or_404(HotelRoom, id=room_id)
        room.is_clean = not room.is_clean
        room.save()
    return redirect('dashboard')