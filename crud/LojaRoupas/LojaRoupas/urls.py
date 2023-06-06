
from django.contrib import admin
from django.urls import include, path
from produtos import urls as produtos_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(produtos_urls)),
    path('', include(produtos_urls))
]
