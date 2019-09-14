# Generated by Django 2.2.5 on 2019-09-14 01:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_provider', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speed', models.FloatField()),
                ('wrong_keys', models.IntegerField()),
                ('correct_keys', models.IntegerField()),
                ('time', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='TestText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='test_provider.Record')),
                ('text', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_provider.TestText')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]