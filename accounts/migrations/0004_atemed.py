# Generated by Django 5.0.8 on 2025-01-14 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_customuser_identification_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atemed',
            fields=[
                ('Atemed_id', models.AutoField(primary_key=True, serialize=False)),
                ('Atemed_Prof_id', models.IntegerField()),
                ('Atemed_Pcte_Id', models.IntegerField()),
                ('Atemed_Ent_id', models.IntegerField()),
                ('Atemed_Fecha_Inicio', models.DateField()),
                ('Atemed_Hora_Inicio', models.TimeField()),
                ('Atemed_Fecha_Fin', models.DateField()),
                ('Atemed_Hora_Fin', models.TimeField()),
                ('Atemed_Diagnostico_CIE10', models.CharField(max_length=255)),
                ('Atemed_Not_Oblig', models.TextField()),
                ('Atemed_Tipo_Diag', models.CharField(max_length=50)),
                ('Atemed_Cron_Diag', models.CharField(max_length=50)),
                ('Atemed_Con_Diagnostico', models.CharField(max_length=50)),
                ('Atemed_Tipo_Ate', models.CharField(max_length=50)),
                ('Atemed_Receta', models.TextField()),
                ('F16', models.CharField(blank=True, max_length=255, null=True)),
                ('F17', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'Atemed$',
            },
        ),
    ]
