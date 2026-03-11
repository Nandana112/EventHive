from django.urls import path
from Adminapp import views

urlpatterns = [
    path('Dashboard/',views.Dashboard,name='Dashboard'),
    path('Events/',views.Events,name='Events'),
    path('Event_Category/',views.Event_Category,name='Event_Category'),
    path('View_Category/',views.View_Category,name='View_Category'),
    path('View_Event/',views.View_Event,name='View_Event'),
    path('Admin_Login/',views.Admin_Login,name='Admin_Login'),
    path('Admin_Logout/',views.Admin_Logout,name='Admin_Logout'),
    path(' Admin_Loginpage/',views.Admin_Loginpage,name='Admin_Loginpage'),
    path('save_category/',views.save_category,name='save_category'),
    path('save_event/',views.save_event,name='save_event'),
    path('delete_event/<int:bk_id>/',views.delete_event,name='delete_event'),
    path('delete_category/<int:cat_id>/',views.delete_category,name='delete_category'),
    path('edit_event/<int:bk_id>/',views.edit_event,name='edit_event'),
    path('edit_category/<int:cat_id>/',views.edit_category,name='edit_category'),
    path('update_event/<int:bk_id>/',views.update_event,name='update_event'),
    path('update_category/<int:cat_id>/',views.update_category,name='update_category'),
    path('Contact_details/',views.Contact_details,name='Contact_details'),
    path('delete_contact/<int:con_id>/',views.delete_contact,name='delete_contact'),


]