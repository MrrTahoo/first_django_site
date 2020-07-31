
from django.contrib import admin
from django.urls import path
from.import navigator

urlpatterns = (
    path('admin/', admin.site.urls),
    path('', navigator.viewer, name='web_view'),
    path('removepunc', navigator.removepunc, name="text_analyze"),

)
