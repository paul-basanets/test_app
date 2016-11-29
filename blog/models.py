# coding: utf-8
from django.db import models


class Topic(models.Model):
    title = models.CharField(max_length=200)


# После создания или изменения модели надо делать manage.py makemigrations и manage.py migrate
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    order = models.PositiveSmallIntegerField(default=0)
    # auto_now_add = True - дата будет установлена при создании объекта
    cdate = models.DateTimeField(auto_now_add=True)
    # auto_now = True - дата будет установлена при редактировании объекта
    edate = models.DateTimeField(auto_now=True)
    topic = models.ForeignKey(Topic, related_name='posts', blank=True, null=True)

    def __unicode__(self):
        return self.title

