from django.urls import path
from .views import negociacoes_kanban_view, negociacoes_list_view, negociacao_details_view
from apps.views import(
    apps_calendar_view,
    apps_calendar_month_grid_view,
    apps_chat_view,
    apps_mailbox_view,
    apps_basicaction_view,
    apps_invoiceaction_view,
    apps_ecommerce_products_view,
    apps_ecommerce_product_details_view,
    apps_ecommerce_add_product_view,
    apps_ecommerce_orders_view,
    apps_ecommerce_update_orders_view,
    apps_ecommerce_delete_orders_view,
    apps_ecommerce_order_details_view,
    apps_ecommerce_customers_view,
    apps_ecommerce_update_customers_view,
    apps_ecommerce_delete_customers_view,
    apps_ecommerce_cart_view,
    apps_ecommerce_checkout_view,
    apps_ecommerce_sellers_view,
    apps_ecommerce_seller_details_view,
    apps_projects_list_view,
    apps_projects_overview_view,
    apps_projects_create_view,
    apps_tasks_kanban_view,
    apps_tasks_list_view,
    apps_tasks_details_view,
    apps_crm_contacts_view,
    apps_crm_add_contacts_view,
    apps_crm_update_contacts_view,
    apps_crm_delete_contacts_view,
    apps_crm_companies_view,
    apps_crm_add_companies_view,
    apps_crm_update_companies_view,
    apps_crm_delete_companies_view,
    apps_crm_deals_view,
    apps_crm_leads_view,
    apps_crm_update_leads_view,
    apps_crm_delete_leads_view,
    apps_crypto_transactions_view,
    apps_crypto_buy_sell_view,
    apps_crypto_orders_view,
    apps_crypto_wallet_view,
    apps_crypto_ico_view,
    apps_crypto_kyc_view,
    apps_invoices_list_view,
    apps_invoices_details_view,
    apps_invoices_create_view,
    apps_tickets_list_view,
    apps_tickets_update_list_view,
    apps_tickets_delete_list_view,
    apps_tickets_details_view,
    apps_nft_marketplace_view,
    apps_nft_explore_view,
    apps_nft_liveauction_view,
    apps_nft_itemdetails_view,
    apps_nft_collections_view,
    apps_nft_creators_view,
    apps_nft_ranking_view,
    apps_nft_wallet_view,
    apps_nft_create_view,

    apps_job_application_view,
    apps_job_update_application_view,
    apps_job_delete_application_view,
    apps_job_candidate_grid_view,
    apps_job_candidate_lists_view,
    apps_job_companies_lists_view,
    apps_job_categories_view,
    apps_job_details_view,
    apps_job_grid_lists_view,
    apps_job_lists_view,
    apps_job_new_view,
    apps_job_statistics_view,
    
    apps_file_manager_view,
    apps_todo_view,
    apps_api_key_view
)
app_name = "apps"

urlpatterns = [
    path('kanban/negociacoes/', negociacoes_kanban_view, name='kanban_negociacoes'),
    path('list/negociacoes/', negociacoes_list_view, name='list_negociacoes'),
    path('detalhes/negociacao/<int:id_negociacao>/', negociacao_details_view, name='detalhes_negociacao'),


    # Calendar
    path("calendar", view=apps_calendar_view, name="calendar"),
    path("calendar_month_grid", view=apps_calendar_month_grid_view, name="calendar_month_grid"),
    # Chat
    path("chat", view=apps_chat_view, name="chat"),
    path("mailbox", view=apps_mailbox_view, name="mailbox"),
    path("basicaction", view=apps_basicaction_view, name="basicaction"),
    path("invoiceaction", view=apps_invoiceaction_view, name="invoiceaction"),

    # Ecommerce
    path("ecommerce/products", view=apps_ecommerce_products_view, name="ecommerce.products"),
    path("ecommerce/product-details", view=apps_ecommerce_product_details_view, name="ecommerce.product_details"),
    path("ecommerce/add-product", view=apps_ecommerce_add_product_view, name="ecommerce.add_product"),
    path("ecommerce/orders", view=apps_ecommerce_orders_view, name="ecommerce.orders"),
    path("ecommerce/update-orders/<int:pk>", view=apps_ecommerce_update_orders_view, name="ecommerce.update_orders"),
    path("ecommerce/delete-orders/<int:pk>", view=apps_ecommerce_delete_orders_view, name="ecommerce.delete_orders"),
    path("ecommerce/order-details", view=apps_ecommerce_order_details_view, name="ecommerce.order_details"),
    path("ecommerce/customers", view=apps_ecommerce_customers_view, name="ecommerce.customers"),
    path("ecommerce/update-customers/<int:pk>", view=apps_ecommerce_update_customers_view, name="ecommerce.update_customers"),
    path("ecommerce/delete-customers/<int:pk>", view=apps_ecommerce_delete_customers_view, name="ecommerce.delete_customers"),
    path("ecommerce/cart", view=apps_ecommerce_cart_view, name="ecommerce.cart"),
    path("ecommerce/checkout", view=apps_ecommerce_checkout_view, name="ecommerce.checkout"),
    path("ecommerce/sellers", view=apps_ecommerce_sellers_view, name="ecommerce.sellers"),
    path("ecommerce/seller-details", view=apps_ecommerce_seller_details_view, name="ecommerce.seller_details"),
    # Projects
    path("projects/list", view=apps_projects_list_view, name="projects.list"),
    path("projects/overview", view=apps_projects_overview_view, name="projects.overview"),
    path("projects/create", view=apps_projects_create_view, name="projects.create"),
    # Tasks
    path("tasks/kanban", view=apps_tasks_kanban_view, name="tasks.kanban"),
    path("tasks/list", view=apps_tasks_list_view, name="tasks.list"),
    path("tasks/details", view=apps_tasks_details_view, name="tasks.details"),
    # CRM Contacts Url
    path("crm/contacts/<int:pk>", view=apps_crm_contacts_view, name="crm.contacts_details"),
    path("crm/contacts", view=apps_crm_add_contacts_view, name="crm.contacts"),
    path("crm/update-contacts/<int:pk>", view=apps_crm_update_contacts_view, name="crm.update_contacts"),
    path("crm/delete-contacts/<int:pk>", view=apps_crm_delete_contacts_view, name="crm.delete_contacts"),
    
    # Crm Companies Url
    
    path("crm/companies", view=apps_crm_add_companies_view, name="crm.companies"),
    path("crm/companies/<int:pk>", view=apps_crm_companies_view, name="crm.companies_details"),
    path("crm/update_companies/<int:pk>", view=apps_crm_update_companies_view, name="crm.update_companies"),
    path("crm/delete-companies/<int:pk>", view=apps_crm_delete_companies_view, name="crm.delete_companies"),
    path("crm/deals", view=apps_crm_deals_view, name="crm.deals"),
    
    # Crm leads Url
    path("crm/leads", view=apps_crm_leads_view, name="crm.leads"),
    path("crm/update_leads/<int:pk>", view=apps_crm_update_leads_view, name="crm.update_leads"),
    path("crm/delete-leads/<int:pk>", view=apps_crm_delete_leads_view, name="crm.delete_leads"),
    # Crypto
    path("crypto/transactions", view=apps_crypto_transactions_view, name="crypto.transactions"),
    path("crypto/buy-sell", view=apps_crypto_buy_sell_view, name="crypto.buy_sell"),
    path("crypto/orders", view=apps_crypto_orders_view, name="crypto.orders"),
    path("crypto/wallet", view=apps_crypto_wallet_view, name="crypto.wallet"),
    path("crypto/ico", view=apps_crypto_ico_view, name="crypto.ico"),
    path("crypto/kyc", view=apps_crypto_kyc_view, name="crypto.kyc"),
    # Invoices
    path("invoices/list", view=apps_invoices_list_view, name="invoices.list"),
    path("invoices/details", view=apps_invoices_details_view, name="invoices.details"),
    path("invoices/create", view=apps_invoices_create_view, name="invoices.create"),
    # Support Tickets
    path("support-tickets/list", view=apps_tickets_list_view, name="tickets.list"),
    path("support-tickets/update-list/<int:pk>", view=apps_tickets_update_list_view, name="tickets.update_list"),
    path("support-tickets/delete-list/<int:pk>", view=apps_tickets_delete_list_view, name="tickets.delete_list"),
    path("support-tickets/details", view=apps_tickets_details_view, name="tickets.details"),

    #NFT Pages
    path("nft/marketplace", view=apps_nft_marketplace_view, name="nft.marketplace"),
    path("nft/explore", view=apps_nft_explore_view, name="nft.explore"),
    path("nft/liveauction", view=apps_nft_liveauction_view, name="nft.liveauction"),
    path("nft/itemdetails", view=apps_nft_itemdetails_view, name="nft.itemdetails"),
    path("nft/collections", view=apps_nft_collections_view, name="nft.collections"),
    path("nft/creators", view=apps_nft_creators_view, name="nft.creators"),
    path("nft/ranking", view=apps_nft_ranking_view, name="nft.ranking"),
    path("nft/wallet", view=apps_nft_wallet_view, name="nft.wallet"),
    path("nft/create", view=apps_nft_create_view, name="nft.create"),
    
    #Job Pages
    path("job/application", view=apps_job_application_view, name="job.application"),
    path("job/update-application/<int:pk>", view=apps_job_update_application_view, name="job.update_application"),
    path("job/delete-application/<int:pk>", view=apps_job_delete_application_view, name="job.delete_application"),
    path("job/candidate-grid", view=apps_job_candidate_grid_view, name="job.candidate_grid"),
    path("job/candidate-lists", view=apps_job_candidate_lists_view, name="job.candidate_lists"),
    path("job/companies-lists", view=apps_job_companies_lists_view, name="job.companies_lists"),
    path("job/categories", view=apps_job_categories_view, name="job.categories"),
    path("job/details", view=apps_job_details_view, name="job.details"),
    path("job/grid-lists", view=apps_job_grid_lists_view, name="job.grid_lists"),
    path("job/lists", view=apps_job_lists_view, name="job.lists"),
    path("job/new", view=apps_job_new_view, name="job.new"),
    path("job/statistic", view=apps_job_statistics_view, name="job.statistics"),
    

    #File Manager
    path("filemanager", view=apps_file_manager_view, name="filemanager"),

    #ToDO
    path("todo", view=apps_todo_view, name="todo"),
    path("api-key", view=apps_api_key_view, name="api_key"),
]
