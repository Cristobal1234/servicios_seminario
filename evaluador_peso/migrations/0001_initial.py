# Generated by Django 2.0 on 2020-01-19 22:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medidas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imc', models.IntegerField(blank=True, default=-1, verbose_name='Imc')),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('nombre', models.CharField(max_length=80, verbose_name='Nombre')),
                ('nickname', models.CharField(max_length=80, primary_key=True, serialize=False, verbose_name='Nickname')),
                ('password', models.CharField(max_length=80, verbose_name='Password')),
                ('peso', models.IntegerField(verbose_name='Peso')),
                ('estatura', models.IntegerField(verbose_name='Estatura')),
            ],
        ),
        migrations.AddField(
            model_name='medidas',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evaluador_peso.Persona', verbose_name='Paciente'),
        ),
    ]
