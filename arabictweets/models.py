from django.db import models

class TwitterText(models.Model):
    tweet_text = models.CharField('tweet', max_length=300, null=True, blank=True)

    # information about the tweet
    tweet_datetime = models.CharField('tweet_datetime', max_length=50, null=True, blank=True)
    tweet_id = models.CharField('tweet_id', max_length=50, null=True, blank=True)
    tweet_lang = models.CharField('lang', max_length=24, null=True, blank=True)
    tweet_source = models.CharField('tweet_source', max_length=255, null=True, blank=True)

    # user information
    tweet_user_username = models.CharField('username', max_length=30, null=True, blank=True)
    tweet_user_id = models.CharField('userid', max_length=30, null=True, blank=True)
    tweet_user_name = models.CharField('name', max_length=30, null=True, blank=True)
    tweet_user_location = models.CharField('user location', max_length=30, null=True, blank=True)
    tweet_user_timezone = models.CharField('user timezone', max_length=30, null=True, blank=True)
    tweet_user_lang = models.CharField('user lang', max_length=30, null=True, blank=True)

    # tweet origin
    tweet_coordinates_langitude = models.CharField('langitude', max_length=30, null=True, blank=True)
    tweet_coordinates_longitude = models.CharField('longitude', max_length=30, null=True, blank=True)
    # tweet place not necessarily originating from
    tweet_place_country = models.CharField('country', max_length=50, null=True, blank=True) 
    tweet_place_city = models.CharField('city', max_length=50, null=True, blank=True) 
    
     
    def __str__(self):
        return self.tweet_text

    class Meta:
        verbose_name_plural = "tweet_texts"

