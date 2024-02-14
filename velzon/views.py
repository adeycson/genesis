# Primeiramente, adquirimos as credenciais e ferramentas necessárias para garantir que apenas os funcionários autorizados possam acessar esses serviços:
from django.contrib.auth.mixins import LoginRequiredMixin  # Um crachá eletrônico que verifica se o funcionário tem permissão para usar o serviço.
from django.shortcuts import redirect, render  # Funcionários da recepção que direcionam os visitantes para a sala de reuniões correta ou para seus escritórios.
from django.urls import reverse_lazy  # Um sistema de navegação interna que ajuda os funcionários a encontrar rapidamente as salas ou áreas desejadas no escritório.
from allauth.account.views import PasswordChangeView, PasswordSetView  # Especialistas em segurança da informação encarregados de ajudar os funcionários a atualizar ou criar suas senhas.

# Agora, definimos os serviços específicos oferecidos pelo nosso 'escritório' CRM:

class MyPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy("dashboards:dashboard")  # Após um funcionário atualizar sua senha com sucesso, ele é automaticamente redirecionado para o painel principal, onde pode ver uma visão geral das tarefas do dia ou informações importantes sobre clientes.

class MyPasswordSetView(PasswordSetView):
    success_url = reverse_lazy("dashboards:dashboard")  # Semelhantemente, depois de configurar uma nova senha, o funcionário é levado de volta ao painel principal, pronto para começar a trabalhar com as informações dos clientes ou continuar de onde parou.

# Essas 'vistas' funcionam como departamentos dentro do nosso escritório CRM, especializados em ajudar os funcionários a manter suas credenciais seguras. Isso é crucial em um ambiente CRM, onde proteger as informações dos clientes é primordial. Após receberem assistência, os funcionários são reconduzidos ao coração do sistema, o painel de controle, de onde podem gerenciar todas as suas interações com clientes de forma eficaz.
