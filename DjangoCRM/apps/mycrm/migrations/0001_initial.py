# Generated by Django 5.0 on 2023-12-12 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=70)),
                ('last_name', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=70)),
                ('phone', models.CharField(max_length=70)),
                ('city', models.CharField(max_length=70)),
                ('state', models.CharField(max_length=70)),
            ],
        ),
    ]