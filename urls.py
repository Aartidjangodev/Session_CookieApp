from django.urls import path
from .import views
urlpatterns=[
    path('setc/',views.setCookie),
    path('getc/',views.getCookie),
    path('delc/', views.delCookie),
    path('sets/',views.setSession),
    path('gets/',views.getSession),
    path('dels/',views.delSession),
]