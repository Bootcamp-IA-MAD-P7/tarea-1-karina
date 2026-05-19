from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True) # <-- Revisa que esté esta línea
    fecha_publicacion = models.DateField()                # <-- Revisa que esté esta línea
    isbn = models.CharField(max_length=13)                # <-- Revisa que esté esta línea

    def __str__(self):
        return self.titulo