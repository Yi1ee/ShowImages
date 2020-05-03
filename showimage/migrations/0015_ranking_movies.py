# Generated by Django 3.0 on 2020-04-12 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showimage', '0014_delete_ranking_movies'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ranking_movies',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('top_id', models.IntegerField()),
                ('filename', models.CharField(max_length=10)),
                ('cname', models.CharField(max_length=30)),
                ('director', models.CharField(max_length=30)),
                ('actors', models.CharField(max_length=30, null=True)),
                ('enname', models.CharField(max_length=50, null=True)),
                ('releasetime', models.CharField(max_length=20, null=True)),
                ('runtime', models.CharField(max_length=20, null=True)),
                ('types', models.CharField(max_length=10, null=True)),
                ('score', models.CharField(max_length=5, null=True)),
                ('introduction', models.CharField(max_length=500, null=True)),
                ('location', models.CharField(max_length=30, null=True)),
            ],
            options={
                'db_table': 'Ranking_movies',
            },
        ),
    ]