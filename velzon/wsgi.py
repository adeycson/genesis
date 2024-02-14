"""
WSGI config for velzon project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

# Imagine que o escritório de um CRM é um prédio complexo, cheio de diferentes departamentos trabalhando juntos para gerenciar as relações com clientes. O arquivo wsgi.py é como o sistema central de telecomunicações desse escritório.

import os  # Primeiro, trazemos o 'técnico' que sabe como lidar com as configurações do prédio.

from django.core.wsgi import get_wsgi_application  # Aqui temos a central telefônica principal, pronta para conectar chamadas internas e externas.

# Antes de ligar a central, precisamos garantir que ela saiba em qual escritório (projeto Django) está operando e quais são as regras desse lugar.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'velzon.settings')

application = get_wsgi_application()  # Agora, a central está ativada e pronta para gerenciar a comunicação dentro do CRM, conectando as solicitações dos clientes (navegador web) com o servidor e vice-versa.

# Esse sistema de comunicação (WSGI) é essencial para o funcionamento do escritório CRM. Ele garante que todas as solicitações, seja de membros da equipe acessando o banco de dados do cliente ou de clientes interagindo com o site, sejam processadas eficientemente e entregues ao destino correto.
