from django.conf.urls import url, include
from django.contrib import admin
from home.views import render_home_index

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', render_home_index, name="home"),
    url(r'^account/', include('accounts.urls')),
]
