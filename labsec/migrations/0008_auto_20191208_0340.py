# Generated by Django 3.0 on 2019-12-08 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labsec', '0007_auto_20191208_0340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chaves',
            name='d',
            field=models.CharField(max_length=650),
        ),
        migrations.AlterField(
            model_name='chaves',
            name='e',
            field=models.CharField(max_length=650),
        ),
        migrations.AlterField(
            model_name='chaves',
            name='p',
            field=models.CharField(max_length=650),
        ),
        migrations.AlterField(
            model_name='chaves',
            name='q',
            field=models.CharField(max_length=650),
        ),
    ]
