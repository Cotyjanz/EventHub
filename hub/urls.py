from django.urls import path
from . import views

urlpatterns = [
	path('', views.DIY_index, name='DIY_index'),
    path('DIY_signup',views.DIY_signup, name ='DIY_signup'),
    path('DIY_user_page', views.DIY_user_page, name = 'DIY_user_page'),
    path('DIY_create', views.DIY_create, name = 'DIY_create'),
    path('<int:primary_key>/', views.event_detail, name='event_detail')
]
