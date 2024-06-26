# Generated by Django 5.0.1 on 2024-04-14 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SavedNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('url', models.URLField(unique=True)),
                ('saved_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
