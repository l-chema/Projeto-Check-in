from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import login_view, logout_view, listar_adolescentes

urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("", listar_adolescentes, name="listar_adolescentes"),
    path('', views.listar_adolescentes, name='listar_adolescentes'),
    path('novo/', views.criar_adolescente, name='criar_adolescente'),
    path('editar/<int:id>/', views.editar_adolescente, name='editar_adolescente'),
    path('excluir/<int:id>/', views.excluir_adolescente, name='excluir_adolescente'),
    path("login/", auth_views.LoginView.as_view(), name="login"),  # Adiciona a view de login padrão do Django
]


