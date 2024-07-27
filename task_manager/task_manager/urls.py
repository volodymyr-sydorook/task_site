from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Включає вбудовані шляхи для аутентифікації
    path('', include('tasks.urls')),
]
