# Generated by Django 3.0.8 on 2020-11-04 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mandela', '0006_conversas_messagems'),
    ]

    operations = [
        migrations.AddField(
            model_name='comunicados',
            name='de',
            field=models.PositiveIntegerField(default=0, verbose_name='de'),
        ),
        migrations.AddField(
            model_name='comunicados',
            name='de2',
            field=models.CharField(choices=[('aluno', 'aluno'), ('professor', 'professor'), ('directoria', 'directoria')], default='', max_length=10, verbose_name='de_'),
        ),
        migrations.AddField(
            model_name='trabalho',
            name='de',
            field=models.PositiveIntegerField(default=0, verbose_name='de'),
        ),
        migrations.AddField(
            model_name='trabalho',
            name='de2',
            field=models.CharField(choices=[('aluno', 'aluno'), ('professor', 'professor'), ('directoria', 'directoria')], default='', max_length=10, verbose_name='de_'),
        ),
    ]
