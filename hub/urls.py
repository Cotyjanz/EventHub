from django.urls import path
from . import views
from hub.views import register
from django.conf.urls import include



urlpatterns = [
	path('accounts/', include("django.contrib.auth.urls")),
	path('register/', register, name="register"),
	path('', views.DIY_index, name='DIY_index'),
	path('DIY_index', views.DIY_index, name='DIY_index'),
	path('DIY_user_page', views.DIY_user_page, name = 'DIY_user_page'),
	path('DIY_create', views.DIY_create, name = 'DIY_create'),
	path('<int:primary_key>/', views.event_detail, name='event_detail')
]
