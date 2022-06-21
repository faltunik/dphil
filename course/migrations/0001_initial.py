# Generated by Django 4.0.4 on 2022-06-21 05:41

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
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('thumbnail', models.ImageField(blank=True, upload_to='course/thumbnail/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('students', models.ManyToManyField(blank=True, related_name='courses', to=settings.AUTH_USER_MODEL)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teaching_courses', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
