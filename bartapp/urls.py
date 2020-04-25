from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "bartapp"

urlpatterns = [
    path('', views.index, name="index"),
    path("register/", views.register, name="register"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('<int:pk>/<slug:category>/<slug:offer>/', views.offer_detail, name="offer_detail")
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)