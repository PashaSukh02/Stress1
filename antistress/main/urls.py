
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index,name='home'),
    path('adobe',views.adobe, name='about'),
    path('news', views.adobe, name='test_home'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)