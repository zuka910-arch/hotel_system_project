from django.shortcuts import render, redirect, get_object_or_404
from .models import HotelRoom
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    rooms = HotelRoom.objects.all()
    return render(request, 'pages/dashboard.html', {'rooms': rooms})

@login_required
def toggle_clean_status(request, room_id):
    if request.method == 'POST':
        room = get_object_or_404(HotelRoom, id=room_id)
        room.is_clean = not room.is_clean
        room.save()
    return redirect('dashboard')

@login_required
def toggle_occupancy_status(request, room_id):
    if request.method == "POST":
        room = get_object_or_404(HotelRoom, id=room_id)
        room.is_occupied = not room.is_occupied 
        room.save()
        
    return redirect('dashboard')