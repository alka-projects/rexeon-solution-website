# Generated by Django 3.1.6 on 2021-09-17 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rexeonapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ('-created_on',)},
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='publish',
            new_name='created_on',
        ),
        migrations.AddField(
            model_name='blog',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(max_length=265, unique=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=265, unique=True),
        ),
    ]