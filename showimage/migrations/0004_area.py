# Generated by Django 3.0 on 2020-04-04 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showimage', '0003_kind'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=20, unique=True)),
                ('movie', models.ManyToManyField(to='showimage.MoviesForm')),
            ],
            options={
                'db_table': 'Area',
            },
        ),
    ]
