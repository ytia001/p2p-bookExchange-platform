# Generated by Django 5.0.2 on 2024-04-19 00:56

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(5, 'Book Title must be greator than 5 characters')])),
                ('description', models.TextField(blank=True, default='', max_length=500, null=True)),
                ('author', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(5, 'Author(s) must be greator than 5 characters')])),
                ('publisher', models.CharField(blank=True, max_length=100, null=True)),
                ('years', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(max_length=255)),
                ('image_public_id', models.CharField(default='', max_length=255)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='discover.post')),
            ],
        ),
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='pending', max_length=20)),
                ('offerer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offered_trades', to=settings.AUTH_USER_MODEL)),
                ('offerer_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offered_trades', to='discover.post')),
                ('requester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requested_trades', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
