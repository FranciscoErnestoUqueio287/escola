# Generated by Django 3.0.8 on 2020-11-03 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mandela', '0005_auto_20201103_0641'),
    ]

    operations = [
        migrations.CreateModel(
            name='messagems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_de_criacao', models.DateTimeField(auto_now_add=True, verbose_name='data_de_criacao')),
                ('conteudo', models.TextField(blank=True, verbose_name='conteudo')),
                ('arquivo', models.FileField(blank=True, upload_to='arquivos/', verbose_name='arquivo')),
            ],
        ),
        migrations.CreateModel(
            name='conversas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('para', models.PositiveIntegerField(default=0, verbose_name='para')),
                ('de', models.PositiveIntegerField(default=0, verbose_name='de')),
                ('de2', models.CharField(choices=[('aluno', 'aluno'), ('professor', 'professor'), ('directoria', 'directoria')], default='', max_length=10, verbose_name='de_')),
                ('para2', models.CharField(choices=[('aluno', 'aluno'), ('professor', 'professor'), ('directoria', 'directoria')], default='', max_length=10, verbose_name='para_')),
                ('messagem', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='mandela.messagems')),
            ],
        ),
    ]