# Generated by Django 2.0.13 on 2019-05-19 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_friend'),
    ]

    operations = [
        migrations.AddField(
            model_name='friend',
            name='friendship',
            field=models.CharField(choices=[('EM', 'Employment'), ('RE', 'Referral')], default='EM', max_length=2),
        ),
    ]
