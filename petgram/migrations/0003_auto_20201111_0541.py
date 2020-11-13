# Generated by Django 3.0.8 on 2020-11-11 05:41

from django.db import migrations, models
import project.storage_backends


class Migration(migrations.Migration):

    dependencies = [
        ('petgram', '0002_remove_post_pet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, null=True, storage=project.storage_backends.PrivateMediaStorage(), upload_to=''),
        ),
    ]