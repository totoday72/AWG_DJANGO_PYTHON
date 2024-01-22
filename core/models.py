from django.db import models

# Create your models here.
class Rhagencia(models.Model):
    agecod = models.IntegerField(primary_key=True)
    agenom = models.CharField(max_length=40, blank=True, null=True)
    direccion = models.CharField(max_length=40, blank=True, null=True)
    def __str__(self):
        return '{}-{}'.format(self.agecod, self.agenom)

    def save(self):
        super(Rhagencia, self).save()

    class Meta:
        verbose_name_plural = "Rhagencia"


class Rhempleado(models.Model):
    agecod = models.ForeignKey(Rhagencia, on_delete=models.CASCADE)
    nombres = models.CharField(max_length=100, help_text='Nombres de Empleados')
    apellidos = models.CharField(max_length=100, help_text='Apellidos Empleado')

    def __str__(self):
        return '{}:{}'.format(self.Rhagen.agenom, self.nombres)

    def save(self):
        super(Rhempleado, self).save()

    class Meta:
        verbose_name_plural = 'rhempleados'
        unique_together = ('agecod', 'nombres')
