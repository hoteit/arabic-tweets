# Generated by Django 2.2 on 2019-04-02 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SearchKeywords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=64, verbose_name='keyword')),
                ('enabled', models.BooleanField(default=False, verbose_name='enabled')),
            ],
            options={
                'verbose_name_plural': 'keywords',
            },
        ),
        migrations.CreateModel(
            name='TwitterText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweet_text', models.CharField(blank=True, max_length=300, null=True, verbose_name='tweet')),
                ('tweet_datetime', models.DateTimeField(auto_now_add=True, verbose_name='time collected')),
                ('tweet_id', models.CharField(blank=True, max_length=24, null=True, verbose_name='tweet_id')),
                ('tweet_lang', models.CharField(blank=True, max_length=24, null=True, verbose_name='lang')),
                ('tweet_source', models.CharField(blank=True, max_length=24, null=True, verbose_name='tweet_source')),
                ('tweet_user_username', models.CharField(blank=True, max_length=30, null=True, verbose_name='username')),
                ('tweet_user_id', models.CharField(blank=True, max_length=30, null=True, verbose_name='userid')),
                ('tweet_user_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='name')),
                ('tweet_user_location', models.CharField(blank=True, max_length=30, null=True, verbose_name='user location')),
                ('tweet_user_timezone', models.CharField(blank=True, max_length=30, null=True, verbose_name='user timezone')),
                ('tweet_user_lang', models.CharField(blank=True, max_length=30, null=True, verbose_name='user lang')),
                ('tweet_coordinates_langitude', models.CharField(blank=True, max_length=30, null=True, verbose_name='langitude')),
                ('tweet_coordinates_longitude', models.CharField(blank=True, max_length=30, null=True, verbose_name='longitude')),
                ('tweet_place_country', models.CharField(blank=True, max_length=24, null=True, verbose_name='country')),
                ('tweet_place_city', models.CharField(blank=True, max_length=24, null=True, verbose_name='city')),
            ],
            options={
                'verbose_name_plural': 'tweets',
            },
        ),
    ]
