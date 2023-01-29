# Generated by Django 2.2 on 2023-01-27 13:46

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('category', models.CharField(blank=True, max_length=50, null=True)),
                ('due_date', models.DateTimeField()),
                ('max_grade', models.FloatField(blank=True, null=True)),
                ('weight', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)])),
                ('file', models.FileField(blank=True, null=True, upload_to='assignments/')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('student', models.ManyToManyField(related_name='classes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lecture', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='module', to='etl.Class')),
            ],
        ),
        migrations.CreateModel(
            name='Weekly',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weekly', to='etl.Module')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(blank=True, null=True)),
                ('is_announcement', models.BooleanField(default=False)),
                ('hits', models.IntegerField(default=0)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('lecture', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='etl.Class')),
            ],
        ),
        migrations.CreateModel(
            name='ModuleContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='modules/')),
                ('weekly', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='module_content', to='etl.Weekly')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='etl.Post')),
            ],
        ),
        migrations.CreateModel(
            name='ClassEvaluation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_1', models.IntegerField(blank=True, null=True)),
                ('choice_2', models.IntegerField(blank=True, null=True)),
                ('choice_3', models.IntegerField(blank=True, null=True)),
                ('choice_4', models.IntegerField(blank=True, null=True)),
                ('choice_5', models.IntegerField(blank=True, null=True)),
                ('choice_6', models.IntegerField(blank=True, null=True)),
                ('choice_7', models.IntegerField(blank=True, null=True)),
                ('descriptive_1', models.TextField(blank=True, null=True)),
                ('descriptive_2', models.TextField(blank=True, null=True)),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etl.Class')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AssignmentToStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_submitted', models.BooleanField(default=False)),
                ('is_graded', models.BooleanField(default=False)),
                ('score', models.FloatField(default=0)),
                ('file', models.FileField(blank=True, null=True, upload_to='submissions/')),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etl.Assignment')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='assignment',
            name='lecture',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='etl.Class'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='student',
            field=models.ManyToManyField(related_name='assignments', through='etl.AssignmentToStudent', to=settings.AUTH_USER_MODEL),
        ),
    ]
