from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
admin.site.site_header = "Mysite admin"
admin.site.site_title = "Mysite admin"