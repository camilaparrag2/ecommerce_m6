from django.db import models


class Product(models.Model):
    nombre = models.CharField("nombre", max_length=200)
    descripcion = models.TextField("descripción")
    precio = models.DecimalField("precio", max_digits=10, decimal_places=2)
    imagen = models.ImageField("imagen", upload_to="products/", blank=True, null=True)
    stock = models.PositiveIntegerField("stock")
    fecha_creacion = models.DateTimeField("fecha de creación", auto_now_add=True)

    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"

    def __str__(self):
        return self.nombre
