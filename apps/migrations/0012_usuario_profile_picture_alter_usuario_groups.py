# Generated by Django 5.0 on 2023-12-27 14:32

import apps.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0011_empresa_usuario'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pictures/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']), apps.models.validate_file_size], verbose_name='Foto de perfil'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='Os grupos aos quais este usuário pertence. Um usuário obterá todas as permissões concedidas a cada um de seus grupos.', related_name='usuario_groups', related_query_name='usuario', to='auth.group', verbose_name='groups'),
        ),
    ]
