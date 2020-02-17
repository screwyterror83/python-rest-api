from django.urls import path

from profiles_api import views
# from django.conf.urls.i18n import urlpatterns

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view())
]
