# Generated by Django 4.0 on 2022-01-11 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100)),
                ('College', models.CharField(blank=True, max_length=100)),
                ('Email', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]