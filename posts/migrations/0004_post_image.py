# Generated by Django 3.1.7 on 2021-10-02 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_remove_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='def_image.jpg', upload_to='post_image/'),
        ),
    ]