# Generated by Django 2.1.1 on 2018-10-01 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='imdb_rating',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='film',
            name='premiera',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='film',
            name='rok',
            field=models.IntegerField(default=2000),
            preserve_default=False,
        ),
    ]
