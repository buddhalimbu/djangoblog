# Generated by Django 3.1.1 on 2020-09-27 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogWebsite', '0022_auto_20200927_0655'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterSocial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_name', models.CharField(max_length=100, null=True)),
                ('social_url', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]