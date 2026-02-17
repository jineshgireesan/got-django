from django.urls import path
from . import views


urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('characters/', views.characters, name='characters'),
    path('logout/', views.logout_view, name='logout'),
    path('makeadmin/', views.create_admin),
    path('setup/', views.setup_view),  # ← add this line
]