from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50,
                            blank=False,
                            null=False,
                            verbose_name='Nome')
    last_login = models.DateTimeField(verbose_name='Último Login',
                                      auto_now=True)
    email = models.EmailField(max_length=255,
                              blank=False,
                              null=False,
                              unique=True,
                              verbose_name='E-mail')
    password = models.CharField(max_length=50,
                                verbose_name='Password')


class Agent(models.Model):
    name = models.CharField(max_length=50,
                            blank=False,
                            null=False,
                            verbose_name='Nome')
    status = models.BooleanField(verbose_name='Sataus')
    env = models.CharField(max_length=20,
                           verbose_name='Env')
    version = models.CharField(verbose_name='Versão',
                               max_length=5)
    address = models.CharField(max_length=39,
                               verbose_name='Endereço') # IPV4


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
                             verbose_name='Nível')
    data = models.TextField(verbose_name='Informações')
    # arquivado
    # date
    # agent_id
    # user_id
    pass


class Group(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name='Nome')


class GroupUser(models.Model):
    group_id = models.ForeignKey(Group,
                                 on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,
                                on_delete=models.CASCADE)
