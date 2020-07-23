# Generated by Django 3.0.5 on 2020-07-20 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('description', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='main_portfolio/images/')),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]