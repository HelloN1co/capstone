# Generated by Django 2.1 on 2020-10-28 08:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('app', '0003_host_administrator'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('contact', models.CharField(max_length=32)),
                ('telphone', models.CharField(max_length=32)),
                ('address', models.CharField(max_length=128)),
                ('customer_id', models.CharField(max_length=128)),
                ('create_time', models.DateField(auto_now=True)),
                ('groups', models.ManyToManyField(to='auth.Group')),
            ],
            options={
                'verbose_name': 'Choice',
                'verbose_name_plural': 'Choice',
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.CharField(auto_created=True, max_length=32, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=32)),
                ('create_time', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'User',
            },
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('contact', models.CharField(max_length=32)),
                ('telphone', models.CharField(max_length=32)),
                ('address', models.CharField(max_length=128)),
                ('customer_id', models.CharField(max_length=128)),
                ('create_time', models.DateField(auto_now=True)),
                ('groups', models.ManyToManyField(to='auth.Group')),
            ],
            options={
                'verbose_name': 'Poll',
                'verbose_name_plural': 'Poll',
            },
        ),
        migrations.AlterField(
            model_name='host',
            name='administrator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Admin'),
        ),
        migrations.AlterField(
            model_name='host',
            name='core_num',
            field=models.SmallIntegerField(choices=[(2, '2 Cores'), (4, '4 Cores'), (6, '6 Cores'), (8, '8 Cores'), (10, '10 Cores'), (12, '12 Cores'), (14, '14 Cores'), (16, '16 Cores'), (18, '18 Cores'), (20, '20 Cores'), (22, '22 Cores'), (24, '24 Cores'), (26, '26 Cores'), (28, '28 Cores')]),
        ),
        migrations.AlterField(
            model_name='host',
            name='service_type',
            field=models.CharField(choices=[('moniter', 'Moniter'), ('lvs', 'LVS'), ('db', 'Database'), ('analysis', 'Analysis'), ('admin', 'Admin'), ('storge', 'Storge'), ('web', 'WEB'), ('email', 'Email'), ('mix', 'Mix')], max_length=32),
        ),
    ]
