# Generated by Django 5.0.6 on 2024-06-26 08:19

import core.movies.models
import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(default='', max_length=255)),
                ('slug', models.SlugField(default='', max_length=150, unique=True)),
                ('plot', models.TextField(default='', max_length=300)),
                ('poster', models.ImageField(blank=True, upload_to=core.movies.models.movie_image_file_path)),
                ('released_year', models.DateField()),
                ('duration', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-released_year'],
            },
        ),
    ]
