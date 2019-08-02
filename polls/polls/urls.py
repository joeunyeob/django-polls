from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('polls/', include('poll.urls')),
    path('admin/', admin.site.urls)
]