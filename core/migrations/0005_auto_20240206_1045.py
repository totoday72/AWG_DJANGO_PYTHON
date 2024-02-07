# Generated by Django 3.2 on 2024-02-06 16:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0004_alter_rhacademico_desc_academicod'),
    ]

    operations = [
        migrations.AddField(
            model_name='rhacademico',
            name='desc_academico',
            field=models.CharField(default='', help_text='Descripcion de grado Academico', max_length=110),
        ),
        migrations.AlterUniqueTogether(
            name='rhacademico',
            unique_together={('cod_academico', 'desc_academico')},
        ),
    ]