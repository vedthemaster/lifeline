# Generated by Django 3.2.4 on 2021-08-24 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LifelineApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='password',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]