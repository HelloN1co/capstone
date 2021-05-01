# Generated by Django 2.1 on 2020-10-28 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20201028_0813'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.CharField(auto_created=True, max_length=32, primary_key=True, serialize=False)),
                ('mid', models.CharField(max_length=32)),
                ('name', models.CharField(max_length=32)),
                ('srcFilePath', models.CharField(max_length=32)),
                ('destFilePath', models.CharField(max_length=32)),
                ('result', models.CharField(max_length=32)),
                ('create_time', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Check history',
                'verbose_name_plural': 'Check history',
            },
        ),
    ]