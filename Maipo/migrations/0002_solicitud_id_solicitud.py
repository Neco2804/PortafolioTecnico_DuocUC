# Generated by Django 3.1.7 on 2021-07-02 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Maipo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitud',
            name='id_solicitud',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
