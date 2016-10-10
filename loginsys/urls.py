from django.conf.urls import url, include



urlpatterns = [

        url(r'^login/', loginsys.views.login),
        url(r'^logout/', loginsys.views.logout),
    ]