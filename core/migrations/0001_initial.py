# Generated by Django 2.2.17 on 2020-12-30 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=200, null=True)),
                ('subject', models.CharField(max_length=200, null=True)),
                ('message', models.TextField(max_length=500, null=True)),
                ('email', models.EmailField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FilmProduction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media_cdn')),
                ('service_name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NextService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(upload_to='media_cdn')),
                ('description', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OurClients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media_cdn')),
                ('name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clients', models.IntegerField(default=1)),
                ('projects', models.IntegerField(default=1)),
                ('hours_of_support', models.IntegerField(default=1)),
                ('hard_work', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='RadioAdverts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media_cdn')),
                ('title', models.CharField(max_length=100, null=True)),
                ('description', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media_cdn')),
                ('name', models.CharField(max_length=200, null=True)),
                ('position', models.CharField(max_length=200, null=True)),
                ('twitter', models.SlugField(blank=True, max_length=300, null=True)),
                ('facebook', models.SlugField(blank=True, max_length=300, null=True)),
                ('gmail', models.SlugField(blank=True, max_length=300, null=True)),
                ('linked', models.SlugField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_image', models.ImageField(upload_to='media_cdn')),
                ('client_name', models.CharField(max_length=200, null=True)),
                ('client_profession', models.CharField(max_length=100, null=True)),
                ('comment', models.ImageField(max_length=200, null=True, upload_to='')),
            ],
        ),
    ]
