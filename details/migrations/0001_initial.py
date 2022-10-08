# Generated by Django 4.1.1 on 2022-10-05 18:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BackgroundColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('logo_image', models.ImageField(upload_to='logo')),
            ],
        ),
        migrations.CreateModel(
            name='Reklam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('reklam_owner', models.CharField(max_length=200)),
                ('describtion', models.TextField()),
                ('image', models.ImageField(upload_to='reklam_images')),
                ('video', models.FileField(blank=True, null=True, upload_to='reklam_videos')),
                ('read_count', models.PositiveIntegerField(default=0)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Light',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('light', models.BooleanField(default=True)),
                ('light_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='light', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
