# Generated by Django 2.2.5 on 2020-07-04 18:45

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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('code', models.CharField(max_length=6)),
                ('slug', models.SlugField()),
                ('overview', models.TextField(max_length=400)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('course_image', models.FileField(blank=True, null=True, upload_to='')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses_created', to=settings.AUTH_USER_MODEL)),
                ('student', models.ManyToManyField(blank=True, related_name='courses_joined', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('slug', models.SlugField()),
                ('video_url', models.FileField(null=True, upload_to='videos')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='')),
                ('position', models.IntegerField()),
                ('files', models.FileField(blank=True, default='default.jpg', null=True, upload_to='profile_pics')),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='modules', to='lms.Course')),
            ],
        ),
    ]
