# Generated by Django 5.0.6 on 2024-06-17 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0002_challenge_months_challenge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='months_challenge',
            field=models.SlugField(blank=True, editable=False, max_length=20),
        ),
    ]
