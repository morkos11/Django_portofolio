# Generated by Django 3.0.3 on 2020-03-13 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectfiles', '0002_contactme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactme',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.DeleteModel(
            name='UserProfileInfo',
        ),
    ]
