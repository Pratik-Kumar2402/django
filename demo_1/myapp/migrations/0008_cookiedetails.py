# Generated by Django 5.0.1 on 2024-04-09 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_blogpost'),
    ]

    operations = [
        migrations.CreateModel(
            name='CookieDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cookie_name', models.CharField(max_length=30)),
                ('cookie_value', models.CharField(max_length=30)),
            ],
        ),
    ]
