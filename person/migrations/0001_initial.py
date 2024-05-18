# Generated by Django 5.0.6 on 2024-05-18 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone_number', models.SmallIntegerField()),
                ('address', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='person')),
            ],
        ),
    ]
