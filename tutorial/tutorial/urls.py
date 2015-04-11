from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app.views.home', name='home'),
    url(r'^register/$', 'app.views.register', name='register'),
    url(r'^login/$', 'app.views.user_login', name='user_login'),
    url(r'^purchase/$', 'app.views.purchase', name='purchase'),
    url(r'^logout/$', 'app.views.logout_view', name='logout_view'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
