
from django.contrib import admin
from django.contrib.admin import views
from django.urls import path, include
from hotel.views import dashboard, toggle_clean_status, toggle_occupancy_status, create_ticket, resolve_ticket


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', dashboard, name='dashboard'),
    path('toggle_clean/<int:room_id>/' , toggle_clean_status, name='toggle_clean'),
    path('toggle-occupancy/<int:room_id>/', toggle_occupancy_status, name='toggle_occupancy'),
    path('ticket/create/<int:room_id>/', create_ticket, name='create_ticket'),
    path('ticket/resolve/<int:ticket_id>/', resolve_ticket, name='resolve_ticket'),
]
