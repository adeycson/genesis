from django.contrib.auth.models import AbstractUser, Group, Permission
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _
from multiselectfield import MultiSelectField


# Create your models here.

TAG_CHOICES = (
    ('Exiting','Exiting'),
    ('Lead','Lead'),
    ('Long-term','Long-term'),
    ('Partner','Partner'),
)

INDUSTRY_TYPE = (
    ('','Select industry type'),
    ('Computer Industry','Computer Industry'),
    ('Chemical Industries','Chemical Industries'),
    ('Health Services','Health Services'),
    ('Telecommunications Services','Telecommunications Services'),
    ('Textiles: Clothing, Footwear','Textiles: Clothing, Footwear')
)

STATUS_CHOICE = (
    ('Approved','Approved'),
    ('New','New'),
    ('Pending','Pending'),
    ('Rejected','Rejected')
)

TYPE_CHOICE = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time')
)

STATUS = (
    ('Pending','Pending'),
    ('Inprogress','Inprogress'),
    ('Cancelled','Cancelled'),
    ('Pickups','Pickups'),
    ('Returns','Returns'),
    ('Delivered','Delivered')
)

PAYMENT_METHOD = (
    ('Mastercard','Mastercard'),
    ('Visa','Visa'),
    ('COD','COD'),
    ('Paypal','Paypal')
)

PRODUCT = (
    ('Puma Tshirt','Puma Tshirt'),
    ('Adidas Sneakers','Adidas Sneakers'),
    ('350 ml Glass Grocery Container','350 ml Glass Grocery Container'),
    ('American egale outfitters Shirt','American egale outfitters Shirt'),
    ('Galaxy Watch4','Galaxy Watch4'),
    ('Apple iPhone 12','Apple iPhone 12'),
    ('Funky Prints T-shirt','Funky Prints T-shirt'),
    ('USB Flash Drive Personalized with 3D Print','USB Flash Drive Personalized with 3D Print'),
    ('Oxford Button-Down Shirt','Oxford Button-Down Shirt'),
    ('Classic Short Sleeve Shirt','Classic Short Sleeve Shirt'),
    ('Half Sleeve T-Shirts (Blue)','Half Sleeve T-Shirts (Blue)'),
    ('Noise Evolve Smartwatch','Noise Evolve Smartwatch')
)

CUSTOMER_STATUS = (
    ('Active','Active'),
    ('Block','Block')
)

TICKET_STATUS = (
    ('Closed','Closed'),
    ('Inprogress','Inprogress'),
    ('New','New'),
    ('Open','Open')
)

PRIORITY = (
    ('High','High'),
    ('Low','Low'),
    ('Medium','Medium')
)

# Modelo para Empresa
class Empresa(models.Model):
    nome = models.CharField(max_length=255, verbose_name=_('Nome da Empresa'))
    cnpj = models.CharField(max_length=14, unique=True, verbose_name=_('CNPJ'))
    endereco = models.TextField(verbose_name=_('Endereço completo'))
    telefone_contato = models.CharField(max_length=20, verbose_name=_('Telefone de contato'))
    email_contato = models.EmailField(verbose_name=_('E-mail de contato'))
    cor_tema = models.CharField(max_length=7, default='#FFFFFF', verbose_name=_('Cor do Tema'), help_text=_('Insira um código de cor hexadecimal.'))
    logo = models.ImageField(upload_to='logos/', verbose_name=_('Logotipo da Empresa'), null=True, blank=True)

    def __str__(self):
        return self.nome

# Modelo de Usuário Customizado
def validate_file_size(value):
    filesize = value.size
    if filesize > 5242880:  # 5MB
        raise ValidationError(_("O tamanho máximo do arquivo que você pode carregar é de 5 MB"))
    else:
        return value

class Usuario(AbstractUser):
    telefone = models.CharField(max_length=20, verbose_name=_('Telefone de contato'))
    cargo = models.CharField(max_length=255, verbose_name=_('Cargo'))
    empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE, verbose_name=_('Empresa associada'), related_name='usuarios')
    profile_picture = models.ImageField(
        upload_to='profile_pictures/',
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']),
            validate_file_size
        ],
        blank=True, null=True,
        verbose_name=_('Foto de perfil')
    )
    

    # Redefine groups e user_permissions com related_name para evitar conflitos
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_('Os grupos aos quais este usuário pertence. Um usuário obterá todas as permissões concedidas a cada um de seus grupos.'),
        related_name="usuario_groups",
        related_query_name="usuario",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name="usuario_user_permissions",
        related_query_name="usuario",
    )

    def __str__(self):
        # Retorna o nome completo se disponível, caso contrário, o nome de usuário
        return self.get_full_name() or self.username

    class Meta:
        verbose_name = _('Usuário')
        verbose_name_plural = _('Usuários')

class CrmContact(models.Model):
    profile_pic = models.ImageField(upload_to="images/contact",blank=True,null=True)
    name = models.CharField(max_length=150)
    company_name = models.CharField(max_length=150)
    designation = models.CharField(max_length=150)
    email_id = models.EmailField(max_length=150,unique=True)
    phone = models.CharField(max_length=13)
    lead_score = models.IntegerField()
    tags = MultiSelectField(max_length=50,choices=TAG_CHOICES,max_choices=3)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def get_photo_url(self):
        if self.profile_pic and hasattr(self.profile_pic, 'url'):
            return self.profile_pic.url
        else:
            return "/static/images/users/user-dummy-img.jpg"
    
    
class CrmCompany(models.Model):
    logo = models.ImageField(upload_to='images/company',blank=True,null=True)
    name = models.CharField(max_length=150)
    owner_name = models.CharField(max_length=50)
    industry_type = models.CharField(max_length=50,choices=INDUSTRY_TYPE)
    rating = models.CharField(max_length=10)
    location = models.CharField(max_length=150)
    employee = models.CharField(max_length=10)
    website = models.CharField(max_length=150)
    contact_email = models.EmailField(max_length=150,unique=True)
    since = models.IntegerField()
    
    class Meta:
        verbose_name_plural = "Crm Companies"
        
    def get_photo_url(self):
        if self.logo and hasattr(self.logo, 'url'):
            return self.logo.url
        else:
            return "/static/images/users/multi-user.jpg"
    
class CrmLead(models.Model):
    profile_pic = models.ImageField(upload_to='images/leads',blank=True,null=True)
    name = models.CharField(max_length=50)
    company_name = models.CharField(max_length=150)
    lead_score = models.IntegerField()
    phone = models.CharField(max_length=13)
    location = models.CharField(max_length=150)
    tags = MultiSelectField(max_length=50,choices=TAG_CHOICES,max_choices=3)
    create_date = models.DateField()
    
    def get_photo_url(self):
        if self.profile_pic and hasattr(self.profile_pic, 'url'):
            return self.profile_pic.url
        else:
            return "/static/images/users/user-dummy-img.jpg"
        
class JobApplication(models.Model):
    profile_pic = models.ImageField(upload_to='images/job/application',blank=True,null=True)
    company_name = models.CharField(max_length=150)
    designation = models.CharField(max_length=150)
    apply_date = models.DateField()
    contact = models.CharField(max_length=13)
    status = models.CharField(max_length=15,choices=STATUS_CHOICE)
    type = models.CharField(max_length=15,choices=TYPE_CHOICE)
    
class EcommerceOrder(models.Model):
    name = models.CharField(max_length=150)
    product = models.CharField(max_length=150,choices=PRODUCT)
    order_date = models.DateTimeField()
    amount = models.CharField(max_length=10)
    payment_method = models.CharField(max_length=50,choices=PAYMENT_METHOD)
    status = models.CharField(max_length=30,choices=STATUS)
    
class EcommerceCustomer(models.Model):
    name = models.CharField(max_length=50)
    email_id = models.EmailField(max_length=50,unique=True)
    phone = models.CharField(max_length=13)
    joining_date = models.DateField()
    status = models.CharField(max_length=12,choices=CUSTOMER_STATUS)
    
class TicketList(models.Model):
    title = models.CharField(max_length=150)
    client_name = models.CharField(max_length=100)
    assign_to = models.CharField(max_length=150)
    create_date = models.DateField()
    due_date = models.DateField()
    status = models.CharField(max_length=10,choices=TICKET_STATUS)
    priority = models.CharField(max_length=10,choices=PRIORITY)
    