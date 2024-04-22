# Generated by Django 4.2.11 on 2024-04-20 09:23

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='image',
            field=models.ImageField(default='default/user.jpg', upload_to=users.models.CustomUser.image_upload_to),
        ),
    ]
