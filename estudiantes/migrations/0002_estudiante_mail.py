# Generated by Django 2.2.24 on 2021-07-05 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiantes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='mail',
            field=models.CharField(default='mail', max_length=200),
            preserve_default=False,
        ),
    ]
