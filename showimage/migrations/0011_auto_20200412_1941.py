# Generated by Django 3.0 on 2020-04-12 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('showimage', '0010_ranking_movies'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='heat_movies',
            name='enname',
        ),
        migrations.RemoveField(
            model_name='heat_movies',
            name='releasetime',
        ),
        migrations.RemoveField(
            model_name='heat_movies',
            name='types',
        ),
    ]
