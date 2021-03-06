# Generated by Django 3.0.3 on 2020-03-12 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectfiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('message', models.TextField()),
            ],
        ),
    ]
