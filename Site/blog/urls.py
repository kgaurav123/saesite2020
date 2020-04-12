from django.urls import path
from . import views

from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from Site import settings

urlpatterns=[
				path('',views.home,name='home'),
				path('bsignup/',views.signup,name='bsignup'),
				path('blogin/',views.login_view,name='blogin'),
				path('blogout/',views.logout_view,name='blogout'),
				path('bupdate/',views.update_profile,name='bupdate'),
				path('create_post/',views.create_post,name='create_post'),
				path('posts/<key>/',views.post_details,name='post_details'),
				path('posts/<key>/confirm_delete/',views.confirm_delete,name='confirm_delete'),
				path('posts/<key>/confirm_delete/deleted',views.post_delete,name='post_delete'),
				path('posts/<key>/create_comment',views.create_comment,name='create_comment'),
				path('posts/<key>/likes',views.create_like,name='likes'),
				#path('view_profile/<key>',views.view_profile,name='profile_view'),
			]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
