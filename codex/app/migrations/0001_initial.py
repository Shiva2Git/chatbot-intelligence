# Generated by Django 4.1.6 on 2023-03-06 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phrase', models.CharField(max_length=200)),
                ('ai_image', models.ImageField(upload_to='images')),
            ],
        ),
    ]
