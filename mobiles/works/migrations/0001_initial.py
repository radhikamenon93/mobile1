# Generated by Django 4.2.6 on 2023-12-07 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=20)),
                ('price', models.PositiveIntegerField()),
                ('year', models.PositiveIntegerField()),
                ('color', models.CharField(max_length=20)),
            ],
        ),
    ]
