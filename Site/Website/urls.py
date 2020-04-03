from django.urls import path
from .import views

from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from Site import settings

urlpatterns = [
    path('',views.index,name='index'),
    path('baja/',views.baja,name='baja'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('update/',views.update_profile,name='update_profile'),
    path('events/',views.events,name='events'),
    path('members/',views.members,name='members'),
    path('events/event_detail/<int:pk>',views.event_details,name='event_details'),
    
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)