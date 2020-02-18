from django.contrib import admin
from django.urls import path
from django.urls import re_path
from portfolio import views
from django.conf import settings
from django.conf.urls.static import static

# Note that the use of the name Experience, Experiences, and work all sort of used interchangeably throughout

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', views.home, name='home'),
    path('awards/', views.certs, name='awards'),
    re_path(r'^work/(\d+)/', views.work_info, name='work'),  # different content pages
    re_path(r'^project/(\d+)/', views.project_info, name='project')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)