# Generated by Django 4.2.7 on 2023-11-24 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mood_tracker', '0005_auto_20231122_2324'),
    ]

    operations = [
        migrations.AddField(
            model_name='diary',
            name='mood',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='diary',
            name='sleep',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]