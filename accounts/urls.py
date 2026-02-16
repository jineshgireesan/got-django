from django.urls import path
from . import views
from accounts.views import create_admin

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('characters/', views.characters, name='characters'),
    path('logout/', views.logout_view, name='logout'),
    path('create-admin/', views.create_admin),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create-admin/', create_admin),   # ADD THIS
    path('', include('accounts.urls')),
]