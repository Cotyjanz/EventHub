from django.urls import path
from . import views
from django.conf.urls import include



urlpatterns = [
	path('accounts/', include("django.contrib.auth.urls")),
	path('register/', views.register, name="register"),
	path('login/', views.signin, name="login"),
  	path('logout/', views.signout, name="logout"),
	path('', views.DIY_index, name='DIY_index'),
	path('DIY_index', views.DIY_index, name='DIY_index'),
	path('DIY_user_page', views.DIY_user_page, name = 'DIY_user_page'),
	path('DIY_create', views.DIY_create, name = 'DIY_create'),
	path('DIY_layout', views.DIY_layout, name = 'DIY_layout'),
   	path('DIY_layout2', views.DIY_layout2, name = 'DIY_layout2'),
	path('<int:primary_key>/', views.event_detail, name='event_detail')
]
