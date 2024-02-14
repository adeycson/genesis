"""velzon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Importamos os componentes essenciais para definir as rotas e a lógica de acesso dentro do nosso sistema Django:
from django.contrib import admin  # O módulo de administração do Django, permitindo gerenciar os dados do sistema através de uma interface web.
from django.urls import path, include  # Ferramentas para definir as URLs (endereços web) e incluir conjuntos de URLs de outras apps no projeto.
from django.contrib.auth.decorators import login_required  # Um decorador que exige que o usuário esteja autenticado para acessar certas views.
from .views import MyPasswordChangeView, MyPasswordSetView  # Views personalizadas para alterar e definir a senha do usuário.
from django.conf.urls.static import static  # Utilitário para servir arquivos estáticos e de mídia durante o desenvolvimento.
from django.conf import settings  # Importa as configurações do projeto para acessar variáveis como DEBUG e configurações de arquivos estáticos/mídia.

# Definimos as rotas (URLs) do nosso sistema, que funcionam como o sistema de navegação, direcionando os usuários para as diferentes partes da aplicação:
urlpatterns = [
    path('admin/', admin.site.urls),  # Rota para o painel de administração, uma área reservada para administradores do sistema.
    path('', include('dashboards.urls')),  # Rota raiz que inclui as URLs do app 'dashboards', normalmente a página inicial do sistema.
    path('apps/', include('apps.urls')),  # Inclui as URLs do app 'apps', dedicado a funcionalidades específicas do sistema.
    path('layouts/', include('layouts.urls')),  # Inclui as URLs do app 'layouts', que pode ser usado para definir diferentes layouts ou temas.
    path('components/', include('components.urls')),  # Inclui as URLs do app 'components', onde componentes reutilizáveis são definidos.
    path('pages/', include('pages.urls')),  # Inclui as URLs do app 'pages', dedicado a páginas estáticas ou dinâmicas do sistema.
    path("account/password/change/", login_required(MyPasswordChangeView.as_view()), name="account_change_password"),  # Rota para alteração de senha, protegida para que apenas usuários autenticados possam acessá-la.
    path("account/password/set/", login_required(MyPasswordSetView.as_view()), name="account_set_password"),  # Rota para definição de senha, também protegida por autenticação.
    path('account/', include('allauth.urls')),  # Inclui as rotas do 'django-allauth' para autenticação, registro e gestão de contas.
]

# Durante o desenvolvimento (quando DEBUG é True), essa configuração adicional permite servir arquivos de mídia através do servidor Django:
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
