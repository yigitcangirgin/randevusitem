from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('' , views.index , name='danisman_index'),
    path('<int:danisman_id>' , views.danisman_details , name='danisman_details'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)