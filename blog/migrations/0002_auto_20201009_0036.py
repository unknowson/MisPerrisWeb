# Generated by Django 3.1.2 on 2020-10-09 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rescatados',
            old_name='rescatado',
            new_name='estado',
        ),
        migrations.AlterField(
            model_name='rescatados',
            name='fotografia',
            field=models.CharField(max_length=200),
        ),
    ]