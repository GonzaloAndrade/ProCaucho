from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
from Home import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'ProCaucho.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', TemplateView.as_view(template_name='Home/index.html')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^contact/$', views.contact, name='contact'),
]