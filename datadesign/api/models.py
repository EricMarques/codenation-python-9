from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.core.validators import validate_email, validate_ipv46_address


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50,
                            blank=False,
                            null=False,
                            verbose_name='Nome',
                            help_text='Nome')
    last_login = models.DateTimeField(verbose_name='Último Login',
                                      auto_now=True)
    email = models.EmailField(max_length=255,
                              blank=False,
                              null=False,
                              unique=True,
                              verbose_name='E-mail',
                              help_text='E-mail',
                              validators=[validate_email])
    password = models.CharField(max_length=50,
                                verbose_name='Password',
                                help_text='Password',
                                validators=[MinLengthValidator(8)])

    class Meta():
        verbose_name='Usuário'


class Agent(models.Model):
    name = models.CharField(max_length=50,
                            blank=False,
                            null=False,
                            verbose_name='Nome',
                            help_text='Nome')
    status = models.BooleanField(verbose_name='Sataus')
    env = models.CharField(max_length=20,
                           verbose_name='Env',
                           help_text='Env.')
    version = models.CharField(verbose_name='Versão',
                               max_length=5,
                               help_text='Versão')
    address = models.GenericIPAddressField(max_length=39,
                                           verbose_name='Endereço',
                                           help_text='Endereço IPV4/IPV6',
                                           validators=[validate_ipv46_address])

    class Meta():
        verbose_name='Agente'


class Event(models.Model):
    LEVEL_CHOICES = [('CRITICAL', 'CRITICAL'),
                     ('DEBUG', 'DEBUG'),
                     ('ERROR', 'ERROR'),
                     ('WARNING', 'WARNING'),
                     ('INFO', 'INFO')
                     ]
    level = models.CharField(max_length=20,
                             choices=LEVEL_CHOICES,
                             null=False,
                             blank=False,
                             verbose_name='Nível',
                             help_text='Nível')
    data = models.TextField(verbose_name='Informações',
                            help_text='Observações')
    arquivado = models.BooleanField(verbose_name='Arquivado')
    date = models.DateField(verbose_name='Data',
                            auto_now=False,
                            help_text='Data')
    agent = models.ForeignKey(Agent,
                                 on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User,
                                on_delete=models.DO_NOTHING)

    class Meta():
        verbose_name='Evento'


class Group(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name='Nome',
                            help_text='Nome')

    class Meta():
        verbose_name='Grupo'


class GroupUser(models.Model):
    group = models.ForeignKey(Group,
                                 on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User,
                                on_delete=models.DO_NOTHING)

    class Meta():
        verbose_name='Grupo de Usuário'