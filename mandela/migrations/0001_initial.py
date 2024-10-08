# Generated by Django 3.0.8 on 2020-11-03 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='nome')),
                ('numero_de_processo', models.PositiveIntegerField(verbose_name='numero_de_processo')),
                ('data_de_nascimento', models.DateField(verbose_name='data_de_nascimento')),
                ('data_de_criacao', models.DateTimeField(auto_now_add=True, verbose_name='data_de_criacao')),
                ('imagem', models.ImageField(blank=True, upload_to='alunos/', verbose_name='imagem')),
                ('contacto', models.CharField(default='+258', max_length=13, verbose_name='contacto')),
                ('classe', models.PositiveIntegerField(verbose_name='classe')),
                ('encarregado', models.CharField(max_length=100, verbose_name='encarregado')),
                ('turma', models.CharField(max_length=100, verbose_name='turma')),
                ('turno', models.CharField(choices=[('Diurno', 'Diurno'), ('Noturno', 'Noturno')], max_length=100, verbose_name='turno')),
                ('password', models.CharField(max_length=100, verbose_name='password')),
            ],
        ),
        migrations.CreateModel(
            name='comunicados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comunicado', models.TextField(verbose_name='comunicado')),
                ('data_de_criacao', models.DateTimeField(auto_now_add=True, verbose_name='data_de_criacao')),
                ('comunicando', models.CharField(blank=True, max_length=100, null=True, verbose_name='comunicando')),
                ('arquivo', models.FileField(blank=True, upload_to='arquivos/', verbose_name='arquivo')),
                ('password', models.CharField(max_length=100, verbose_name='password')),
            ],
        ),
        migrations.CreateModel(
            name='conversa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('para', models.PositiveIntegerField(default=0, verbose_name='para')),
                ('de', models.PositiveIntegerField(default=0, verbose_name='de')),
                ('de2', models.CharField(choices=[('aluno', 'aluno'), ('professor', 'professor'), ('directoria', 'directoria')], default='', max_length=10, verbose_name='de_')),
                ('para2', models.CharField(choices=[('aluno', 'aluno'), ('professor', 'professor'), ('directoria', 'directoria')], default='', max_length=10, verbose_name='para_')),
                ('arquivo', models.FileField(blank=True, upload_to='arquivos/', verbose_name='arquivo')),
                ('data_de_criacao', models.DateTimeField(auto_now_add=True, verbose_name='data_de_criacao')),
                ('conteudo', models.TextField(blank=True, verbose_name='conteudo')),
            ],
        ),
        migrations.CreateModel(
            name='directoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='nome')),
                ('data_de_criacao', models.DateTimeField(auto_now_add=True, verbose_name='data_de_criacao')),
                ('data_de_nascimento', models.DateField(verbose_name='data_de_nascimento')),
                ('cargo', models.CharField(blank=True, max_length=100, verbose_name='cargo')),
                ('imagem', models.ImageField(upload_to='directoria/', verbose_name='imagem')),
                ('contacto', models.CharField(default='+258', max_length=13, verbose_name='contacto')),
                ('password', models.CharField(max_length=100, verbose_name='password')),
            ],
        ),
        migrations.CreateModel(
            name='imagens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(upload_to='img/', verbose_name='imagem')),
                ('data_de_criacao', models.DateTimeField(auto_now_add=True, verbose_name='data_de_criacao')),
            ],
        ),
        migrations.CreateModel(
            name='professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='nome')),
                ('data_de_nascimento', models.DateField(verbose_name='data_de_nascimento')),
                ('data_de_criacao', models.DateTimeField(auto_now_add=True, verbose_name='data_de_criacao')),
                ('imagem', models.ImageField(blank=True, upload_to='prof/', verbose_name='imagem')),
                ('contacto', models.CharField(default='+258', max_length=13, verbose_name='contacto')),
                ('turmas', models.CharField(max_length=100, verbose_name='turmas')),
                ('password', models.CharField(max_length=100, verbose_name='password')),
            ],
        ),
        migrations.CreateModel(
            name='trabalho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comunicando', models.CharField(blank=True, max_length=100, verbose_name='comunicando')),
                ('comunicado', models.TextField(blank=True, verbose_name='comunicado')),
                ('data_de_criacao', models.DateTimeField(auto_now_add=True, verbose_name='data_de_criacao')),
                ('arquivo', models.FileField(blank=True, upload_to='arquivos/', verbose_name='arquivo')),
                ('password', models.CharField(max_length=100, verbose_name='password')),
            ],
        ),
        migrations.CreateModel(
            name='turma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referencia', models.CharField(max_length=100, verbose_name='referencia')),
                ('director_de_turma', models.CharField(max_length=100, verbose_name='director_de_turma')),
                ('data_de_criacao', models.DateTimeField(auto_now_add=True, verbose_name='data_de_criacao')),
                ('chefe_de_turma', models.CharField(blank=True, max_length=100, verbose_name='chefe_de_turma')),
                ('classe', models.PositiveIntegerField(verbose_name='classe')),
                ('imagem', models.ImageField(blank=True, upload_to='directoria/', verbose_name='imagem')),
                ('password', models.CharField(max_length=100, verbose_name='password')),
            ],
        ),
    ]
