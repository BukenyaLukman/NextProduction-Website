# Generated by Django 2.2.17 on 2020-12-30 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20201230_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='facebook',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='linked',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='twitter',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]