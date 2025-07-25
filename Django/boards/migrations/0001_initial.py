# Generated by Django 5.2.3 on 2025-06-18 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('writer', models.CharField(max_length=30)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('likes', models.PositiveIntegerField(default=0)),
                ('reviews', models.PositiveIntegerField(default=0)),
                ('details', models.CharField(max_length=30)),
            ],
        ),
    ]
