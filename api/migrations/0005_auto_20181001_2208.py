# Generated by Django 2.1.1 on 2018-10-01 22:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20181001_2149'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aktor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=32)),
                ('nazwisko', models.CharField(max_length=32)),
                ('filmy', models.ManyToManyField(to='api.Film')),
            ],
        ),
        migrations.AlterField(
            model_name='extrainfo',
            name='rodzaj',
            field=models.IntegerField(choices=[(3, 'Drama'), (0, 'Nieznany'), (4, 'Komedia'), (2, 'Sci-fi'), (1, 'Horror')], default=0),
        ),
        migrations.AlterField(
            model_name='recenzja',
            name='film',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recenzje', to='api.Film'),
        ),
    ]