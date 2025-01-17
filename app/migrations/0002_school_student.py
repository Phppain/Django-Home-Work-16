# Generated by Django 5.1.4 on 2024-12-09 16:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('adress', models.CharField(max_length=255)),
                ('institution_type', models.CharField(choices=[('PRЧастная', 'Private'), ('PBГосударственная', 'Public')], max_length=255)),
                ('status', models.CharField(choices=[('GMГимназия', 'Gymnasium'), ('LCЛицей', 'Lyceum'), ('GEОбщеобразовательная', 'General Education')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('birth_date', models.DateField()),
                ('student_class', models.CharField(max_length=3)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.school')),
            ],
        ),
    ]
