# Generated by Django 2.1.7 on 2019-03-14 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_merge_20190312_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='connorhead.png', upload_to='profile_pics'),
        ),
    ]
