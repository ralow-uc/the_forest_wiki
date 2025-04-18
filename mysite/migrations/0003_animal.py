# Generated by Django 5.1.7 on 2025-04-18 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_alter_construccion_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='animales/')),
                ('hostilidad', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
            ],
        ),
    ]
