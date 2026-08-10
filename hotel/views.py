from django.shortcuts import render, redirect, get_object_or_404
from .models import HotelRoom, Ticket
from django.contrib.auth.decorators import login_required
from django.utils import timezone


@login_required
def dashboard(request):
    rooms = HotelRoom.objects.all()
    
    is_reception = request.user.groups.filter(name='Reception').exists()
    is_housekeeping = request.user.groups.filter(name='Housekeeping').exists()
    is_facchini = request.user.groups.filter(name='Facchini').exists()
    context = {
        'rooms': rooms,
        'is_reception': is_reception,
        'is_housekeeping': is_housekeeping,
        'is_facchini': is_facchini,
    }
    
    return render(request, 'pages/dashboard.html', context)

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

@login_required
def create_ticket(request, room_id):
    room = get_object_or_404(HotelRoom, id=room_id)
    
    if request.method == "POST":
        informazione_text = request.POST.get('informazione', '')
        if informazione_text:
            Ticket.objects.create(
                room=room,
                informazione=informazione_text
            )
            
    return redirect('dashboard')

@login_required
def resolve_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id =ticket_id)
    if request.method == 'POST':
        reply_text = request.POST.get('reply', '')

        ticket.reply = reply_text
        ticket.is_done = True
        ticket.resolved_at = timezone.now()
        ticket.save()
        return redirect('dashboard')