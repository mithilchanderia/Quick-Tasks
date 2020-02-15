from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('delete/<list_id>',views.delete,name='delete'),
    path('cross_off/<list_id>',views.cross_off,name='cross_off'),
    path('cross_on/<list_id>',views.cross_on,name='cross_on'),
    path('edit/<list_id>',views.edit,name='edit'),
]
