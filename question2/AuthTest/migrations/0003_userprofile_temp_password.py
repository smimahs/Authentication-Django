# Generated by Django 3.0.8 on 2020-12-03 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AuthTest', '0002_auto_20201202_2359'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='temp_password',
            field=models.CharField(default=0, max_length=5),
            preserve_default=False,
        ),
    ]
