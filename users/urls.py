from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout_then_login

from users.views import RegistroUsuario

urlpatterns = [
    url(r'^registrar', RegistroUsuario.as_view(), name='registrar_usuario'),

]