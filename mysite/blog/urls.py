from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
            path('post/<int:pk>/',  views.post_detail, 
        name='post_inhoud'),
                path('post/nieuw/',  views.post_nieuw, 
        name='post_nieuw'),
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
]