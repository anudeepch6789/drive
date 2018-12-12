from django.conf.urls import include, url
from . import views


urlpatterns = [
   # url(r'^$',views.home,name='home'),
    url(r'^signup/',views.signup,name='signup'),
   # url(r'^after_signup/$',views.after_signup,name='after_signup'),


]