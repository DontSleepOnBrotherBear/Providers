# Generated by Django 2.0.13 on 2019-05-19 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190519_0608'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('providers', models.ManyToManyField(to='blog.Provider')),
            ],
        ),
    ]