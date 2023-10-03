from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
# Create your models here.

RESCATADOX = (('disponible','Disponible'),('rescatado','Rescatado'),('adoptado','Adoptado'))

class Rescatados(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    fotografia = models.CharField(max_length=200, blank=False, null=False)
    nombre = models.CharField(max_length=20, blank=False, null=False)
    raza_dominante = models.CharField(max_length=20, blank=False, null=False)
    descripcion = models.TextField( blank=False, null=False)
    estado=models.CharField(max_length=10, choices=RESCATADOX)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nombre