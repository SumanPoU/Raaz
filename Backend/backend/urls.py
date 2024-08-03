from django.contrib import admin
from django.urls import path, include

admin.site.site_header = 'Razza Admin'
admin.site.site_title = 'Razza Admininstation Portal'
admin.site.index_title = 'Welcome to Razza Admin Portal'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('app_users.urls')),
    path('search/', include('app_citizen_data.urls')),
]
