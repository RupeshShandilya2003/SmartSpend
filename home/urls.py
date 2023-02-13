from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration/',views.home,name="registration"),
    path('table/',views.table,name="table")
]
