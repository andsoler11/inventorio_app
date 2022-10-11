import profile
import uuid
from django.db import models
from django.contrib.auth.models import User

class Products(models.Model):
    id          = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    profile     = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    nombre      = models.CharField(max_length=255)
    cantidad    = models.IntegerField()
    precio      = models.IntegerField()
    fecha       = models.DateField(auto_now_add=True)
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
