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
        db_table = 'core_Rhagencia'


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
        db_table = 'core_rhempleado'


class Rhmotiv(models.Model):
    codmot = models.IntegerField(primary_key=True, help_text='Id del motivo', unique=True)
    # agecod = models.ForeignKey(Rhagencia, on_delete=models.CASCADE)
    nommot = models.CharField(max_length=100, help_text='Descripcion de Motivo')

    def __str__(self):
        return '{}:{}'.format(self.codmot, self.nommot)

    def save(self):
        super(Rhmotiv, self).save()

    class Meta:
        verbose_name_plural = 'Rhmotiv'
        unique_together = ('codmot', 'nommot')
        db_table = 'core_Rhmotiv'

    class rhacademico(models.Model):
        cod_academico = models.AutoField(primary_key=True, help_text='Id del academico', unique=True)
        # agecod = models.ForeignKey(Rhagencia, on_delete=models.CASCADE)
        desc_academico = models.CharField(max_length=110, help_text='Descripcion de grado Academico', default='')

        # desc_academicod = models.CharField(max_length=2, help_text='Descripcion de grado Academico', default=0)

        def __str__(self):
            return '{}:{}'.format(self.codmot, self.nommot)

        def save(self):
            super(Rhmotiv, self).save()

        class Meta:
            verbose_name_plural = 'rhacademico'
            unique_together = ('cod_academico', 'desc_academico')
            db_table = 'core_rhacademico'
