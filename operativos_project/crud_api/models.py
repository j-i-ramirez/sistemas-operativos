from django.db import models

class Item(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'items'