from django.urls import path
from .import views
urlpatterns = [
    path('',views.index,name='index'),
    path('baja/',views.baja,name='baja'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('update/',views.update_profile,name='update_profile'),
    path('member_list/',views.member_list,name='member_list'),
    
    
]