# Generated by Django 3.1 on 2024-04-27 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('text_to_image', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generatedimage',
            name='image_data',
            field=models.BinaryField(),
        ),
    ]