# Generated by Django 4.0.3 on 2022-07-24 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0012_alter_customuser_pin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='u_name',
        ),
    ]
