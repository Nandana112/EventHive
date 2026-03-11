from django.urls import path
from Organizerapp import views
urlpatterns = [
    path('Home/',views.Home,name='Home'),
    path('All_Events/',views.All_Events,name='All_Events'),
    path('About/',views.About,name='About'),
    path('Contact/',views.Contact,name='Contact'),
    path('Booking_details/',views.Booking_details,name='Booking_details'),
    path('save_contact/',views.save_contact,name='save_contact'),
    path('sign_in/',views.sign_in,name='sign_in'),
    path('sign_up/',views.sign_up,name='sign_up'),
    path('user_login/',views.user_login,name='user_login'),
    path('user_logout/',views.user_logout,name='user_logout'),
    path('save_registration/',views.save_registration,name='save_registration'),
    path('filter_events/<eve_name>',views.filter_events,name='filter_events'),
    path('event_single/<int:event_id>',views.event_single,name='event_single'),
    path('save_booking/',views.save_booking,name='save_booking'),
    ]