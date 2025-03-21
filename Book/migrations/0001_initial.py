# Generated by Django 5.1.5 on 2025-01-30 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('translator', models.CharField(blank=True, max_length=100, null=True)),
                ('publisher', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('pages', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Book',
            },
        ),
    ]
