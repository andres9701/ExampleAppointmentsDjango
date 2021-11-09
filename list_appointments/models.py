from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField

# Create your models here.
class RolesUser(models.Model):
    ROLES_TYPE = (
        ("doctor", "Doctor"),
        ("paciente", "Paciente")
    )
    user = models.OneToOneField(User, verbose_name=("User"), on_delete=models.CASCADE)
    rol = models.CharField(choices=ROLES_TYPE,max_length=20)

    class Meta:
        verbose_name = ("Rol User")
        verbose_name_plural = ("Rols User")

    
    def __str__(self):
        return self.user.username



class CustomSettings(models.Model):
    SECTIONS = (
        ("SECTION_ONE",'section one'),
        ("SECTION_tWO",'section two'),
        ("SECTION_THREE",'section three'),
    )
    id_provider = models.SmallIntegerField()
    id_section = models.CharField(choices=SECTIONS,max_length=100)
    configurations =models.JSONField()
    logo = models.ImageField()

    class Meta:
        verbose_name = ("Custom Settings")
        verbose_name_plural = (" Custom Settings")
        
   

    
    def __str__(self):
        return self.id_section



        
