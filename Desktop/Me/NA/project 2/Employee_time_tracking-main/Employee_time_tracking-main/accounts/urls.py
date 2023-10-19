from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='signout'),
    path('home/', views.home, name='home') 
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)