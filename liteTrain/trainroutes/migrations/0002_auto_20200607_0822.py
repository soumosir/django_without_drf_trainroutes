# Generated by Django 3.0.6 on 2020-06-07 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainroutes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='trainroute',
            options={'ordering': ('duration',)},
        ),
    ]
