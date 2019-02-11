from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from projects import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
	path('projects/', include('projects.urls')),
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()
