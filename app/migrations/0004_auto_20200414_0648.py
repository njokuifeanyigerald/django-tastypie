# Generated by Django 3.0.4 on 2020-04-14 05:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tastypie.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0003_auto_20200413_2230'),
    ]

    operations = [
        migrations.CreateModel(
            name='Myway',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('timestamp', models.DateTimeField(default=tastypie.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'my ways',
            },
        ),
        migrations.DeleteModel(
            name='Tastypie',
        ),
    ]
