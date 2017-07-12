from django.conf.urls import url
from django.contrib.auth import views as django_views
from . import views


urlpatterns = [
    #Widoki logowania
    #
    #Poprzedni widok logowania:
    #url(r'^login/$', views.user_login, name='login'),
    #
    #Wzorce adresów url dla widoków logowania i wylogowania
    url(r'^login/$', django_views.login, name='login'),
    url(r'^logout/$', django_views.logout, name='logout'),
    url(r'^logout-then-login/$', django_views.logout_then_login, name='logout_then_login'),
    url(r'^$', views.dashboard, name='dashboard'),
    #Wzorce adresów url do obsługi zmiany hasła
    url(r'^password-change/$', django_views.password_change, name='password_change'),
    url(r'^password-change/done/$', django_views.password_change_done, name='password_change_done'),
    #Wzorce adresów url do obsługi procedury zerowania hasła
    url(r'^password-reset/$', django_views.password_reset, name='password_reset'),
    url(r'^password-reset/done/$', django_views.password_reset_done, name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
        django_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^password-reset/complete/$', django_views.password_reset_complete, name='password_reset_complete'),
]