# Generated by Django 3.1.6 on 2021-09-18 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rexeonapp', '0004_auto_20210917_1755'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=100)),
                ('Last_name', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('Contact_no', models.IntegerField()),
                ('Resume', models.FileField(default=None, upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='Get_in_touch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=50)),
                ('Contact_no', models.IntegerField()),
                ('Queries', models.CharField(max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='blog',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10),
        ),
    ]