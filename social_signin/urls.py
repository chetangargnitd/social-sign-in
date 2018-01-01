from django.conf.urls import url,include
from django.contrib import admin

from task import views as task_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', task_views.home, name = 'home'),
    url(r'^', include('task.urls', namespace ="task")),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
]
