from django.contrib import admin
from django.urls import path
import myapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myapp.views.home, name="home"),

    # http://127.0.0.1:8000/base/
    path('base/', myapp.views.base, name="base"),
]
