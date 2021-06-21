# Generated by Django 3.2.4 on 2021-06-21 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_created=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('actived', models.BooleanField(default=True)),
                ('id_doc', models.IntegerField(default=0)),
                ('path', models.CharField(max_length=255)),
                ('mime_type', models.CharField(max_length=100)),
                ('url', models.URLField(unique=True)),
            ],
            options={
                'verbose_name': 'Documento',
                'verbose_name_plural': 'Dossie',
            },
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_created=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('actived', models.BooleanField(default=True)),
                ('action', models.CharField(max_length=255)),
                ('start_hour', models.DateTimeField(auto_now=True)),
                ('end_hour', models.DateTimeField()),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='histories', to='document.document')),
            ],
            options={
                'verbose_name': 'History',
                'verbose_name_plural': 'Histories',
            },
        ),
    ]