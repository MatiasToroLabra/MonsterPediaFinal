from django.urls import path
from . import views

urlpatterns = [
 	path('',views.index,name='index'),
 	path('login',views.login,name='login'),
 	path('register',views.register,name='register'),
 	path('registersmash',views.registersmash,name='registersmash'),
 	path('monsters', views.MonsterListView.as_view(), name='monsters'),
 	path('armors', views.ArmorListView.as_view(), name='armors'),
    path('monster/<int:pk>', views.MonsterDetailView.as_view(), name='monster-detail'),
    path('armor/<int:pk>', views.ArmorDetailView.as_view(), name='armor-detail'),
]

urlpatterns += [
    path('armor/create/', views.ArmorCreate.as_view(), name='armor_create'),
    path('armor/<int:pk>/update/', views.ArmorUpdate.as_view(), name='armor_update'),
    path('armor/<int:pk>/delete/', views.ArmorDelete.as_view(), name='armor_delete'),
]
