# Generated by Django 5.0 on 2023-12-20 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Finch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('lifespan', models.IntegerField()),
                ('weight', models.IntegerField()),
            ],
        ),
    ]
