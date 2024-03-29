from django.db import models
from mdeditor.fields import MDTextField
from django.utils import timezone


class TalkTags(models.Model):
    name = models.CharField("Talk about tags", max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Talk about tags"
        verbose_name_plural = verbose_name
        ordering = ['id']


class TalkContent(models.Model):

    STATUS = (
        ('y', "Public"),
        ('n', 'Private')
    )

    body = MDTextField('Talk about the text')
    created_time = models.DateTimeField('Creation time', default=timezone.now)
    tag = models.ManyToManyField(TalkTags, verbose_name="Talk about tags")
    status = models.TextField("Post status", choices=STATUS, default='y')

    class Meta:
        verbose_name = "Talk about content"
        verbose_name_plural = verbose_name
        ordering = ['-created_time']
