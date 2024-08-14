from aidiet import urls
from home import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    # path('admin/', admin.site.urls),
   path("", views.signup, name='signup'),
    path("login/", views.login, name='login'),
    path("login/process/", views.process_login, name='process'),
    path("home/", views.home, name='home')
]
