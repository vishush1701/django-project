# Generated by Django 5.0.6 on 2024-06-17 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0003_alter_challenge_months_challenge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='months_challenge',
            field=models.SlugField(blank=True, default='', editable=False, max_length=20),
        ),
    ]
