# Generated by Django 4.2.10 on 2024-04-18 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0003_alter_album_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='src/images')),
            ],
        ),
    ]
