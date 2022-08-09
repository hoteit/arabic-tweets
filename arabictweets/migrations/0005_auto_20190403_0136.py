# Generated by Django 2.2 on 2019-04-03 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arabictweets', '0004_auto_20190402_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twittertext',
            name='tweet_datetime',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='tweet_datetime'),
        ),
        migrations.AlterField(
            model_name='twittertext',
            name='tweet_id',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='tweet_id'),
        ),
        migrations.AlterField(
            model_name='twittertext',
            name='tweet_place_city',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='city'),
        ),
        migrations.AlterField(
            model_name='twittertext',
            name='tweet_place_country',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='country'),
        ),
    ]
