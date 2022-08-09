
# arabic

Arabic NLP research and development

## Twitter Arabic Tweets Collector code setup

1. clone the code from [github](git@github.com:hoteit/arabic.git) or [github](https://github.com/hoteit/arabic.git)
2. if you are starting from scratch, setup the Django code by first create the project called *arabic* `docker-compose run web django-admin startproject arabic .` then create a Docker app called *arabictweets* `docker-compose run web django-admin startapp arabictweets`.
3. Start Django with `docker-compose up`. Note if you need to rebuild the project before starting it, you would run `docker-compose up --build`
A shortcut is available to start docker by executing `start_docker.sh`
4. when developing and making changes to your model, you may need to synchronize the model with the database. You would run `docker-compose run web ./manage.py makemigrations arabictweets` followed by `docker-compose run web manage.py ./migrate arabictweets`.
