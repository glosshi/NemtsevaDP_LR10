from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('traffic/', views.traffic, name='traffic'),
    path('logs/', views.logs, name='logs'),
    path('analytics/', views.analytics, name='analytics'),
    path('blocks/', views.blocks, name='blocks'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)