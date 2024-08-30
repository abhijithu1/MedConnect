from django.urls import path,include
from dj_rest_auth.registration.views import RegisterView

from . import views

urlpatterns = [
     path("auth/register/", RegisterView.as_view(), name="rest_register"),
    path('auth/', include('dj_rest_auth.urls')),
    path("", views.index, name="index"),
]