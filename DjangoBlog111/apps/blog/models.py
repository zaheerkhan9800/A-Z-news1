# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.html import strip_tags
import django.utils.timezone as timezone
from mdeditor.fields import MDTextField


# 创建博文分类的表
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Category Name')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Article classification"
        verbose_name_plural = verbose_name

    def get_absolute_url(self):
        return reverse('blog:category', kwargs={'pk': self.pk})


# 创建文章标签的表
class Tag(models.Model):
    # name是标签名的字段
    name = models.CharField('Label name', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Article tags"
        verbose_name_plural = verbose_name

    def get_absolute_url(self):
        return reverse('blog:tag_list', kwargs={'pk': self.pk})


# 创建文章的类
class Post(models.Model):
    # 发表状态
    PUBLISH_STATUS = (
        ('p', 'Article page'),
        ('c', 'Tutorial page'),
        ('d', 'Draft box'),
        ('r', 'Recycle bin'),
    )

    # 是否置顶
    STICK_STATUS = (
        ('y', 'Top'),
        ('n', 'Not sticky'),
    )

    title = models.CharField('Title', max_length=100, unique=True)
    image=models.ImageField(null=True, blank=True)
    body = MDTextField('Text')
    created_time = models.DateTimeField('Creation time', default=timezone.now)
    modified_time = models.DateTimeField('Modified at', auto_now=True)
    excerpt = models.CharField('Summary', max_length=200, blank=True, )
    views = models.PositiveIntegerField('Reading', default=0)
    words = models.PositiveIntegerField('Word count', default=0)
    category = models.ForeignKey(Category, verbose_name='Article classification', on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, verbose_name='Label type', blank=True)
    # author = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE, default="reborn")
    author = models.ForeignKey(User, verbose_name='Author', on_delete=models.CASCADE)
    status = models.CharField('Article status', max_length=1, choices=PUBLISH_STATUS, default='p')
    stick = models.CharField('Whether to stick', max_length=1, choices=STICK_STATUS, default='n')

    def get_absolute_url(self):
        return reverse('blog:article', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    def get_user(self):
        return self.author

    # 阅读量增加1
    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def save(self, *args, **kwargs):
        if not self.excerpt:
            self.excerpt = strip_tags(self.body).replace("&nbsp;", "").replace("#", "")[:150]
        self.words = len(strip_tags(self.body).replace(" ", "").replace('\n', ""))
        super(Post, self).save(*args, **kwargs)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    class Meta:
        verbose_name = "Add article"
        verbose_name_plural = verbose_name
        ordering = ['-created_time']


class BookCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="Category Name")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Book list classification"
        verbose_name_plural = verbose_name


class BookTag(models.Model):
    name = models.CharField(max_length=100, verbose_name="label")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:book_list', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Book List Label"
        verbose_name_plural = verbose_name


class Book(models.Model):
    name = models.CharField("Title", max_length=100)
    author = models.CharField("Author", max_length=100)
    category = models.ForeignKey(BookCategory, on_delete=models.CASCADE, verbose_name="Book classification")
    tag = models.ManyToManyField(BookTag, verbose_name="Book label")
    cover = models.ImageField("Cover picture", upload_to='books', blank=True)
    score = models.DecimalField("Ratings", max_digits=2, decimal_places=1)
    created_time = models.DateField("Creation time", null=True, default=timezone.now)
    time_consuming = models.CharField("Reading time", max_length=100)
    pid = models.CharField("Article ID", max_length=100, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:article', kwargs={'pk': self.pid})

    class Meta:
        verbose_name = "Add book"
        verbose_name_plural = verbose_name
        ordering = ['-pk']


class MovieCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="Movie classification")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Movie classification"
        verbose_name_plural = verbose_name


class MovieTag(models.Model):
    name = models.CharField(max_length=100, verbose_name="Label name", blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:movie_list', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Movie label"
        verbose_name_plural = verbose_name


class Movie(models.Model):
    name = models.CharField("Movie title", max_length=100)
    director = models.CharField("Director", max_length=100)
    actor = models.CharField("Starring", max_length=100)
    category = models.ForeignKey(MovieCategory, on_delete=models.CASCADE, verbose_name="Movie classification")
    tag = models.ManyToManyField(MovieTag, verbose_name="Movie label")
    cover = models.ImageField("Upload cover", upload_to='movies', blank=True)
    score = models.DecimalField("Rating", max_digits=2, decimal_places=1)
    release_time = models.DateField("Release time")
    created_time = models.DateField("Creation time", default=timezone.now)
    length_time = models.PositiveIntegerField("Movie duration", default=0)
    watch_time = models.DateField("Watch time", default=timezone.now)
    pid = models.CharField("Article ID", max_length=100, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:article', kwargs={'pk': self.pid})

    class Meta:
        verbose_name = "Add movie"
        verbose_name_plural = verbose_name
        ordering = ['-pk']


class Messages(models.Model):
    name = models.CharField(max_length=100, verbose_name="leave me a message")
    admin = models.ForeignKey(User, verbose_name='Webmaster', on_delete=models.CASCADE, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('blog:messages')

    def get_user(self):
        return self.admin

    class Meta:
        verbose_name = "Website Message"
        verbose_name_plural = verbose_name


class MeanList(models.Model):
    STATUS = (
        ('y', 'display'),
        ('n', 'hide'),
    )

    title = models.CharField("Menu name/title", max_length=100)
    link = models.CharField("Menu link", max_length=100, blank=True, null=True, )
    icon = models.CharField("Menu icon", max_length=100, blank=True, null=True, )
    status = models.CharField('Display state', max_length=1, choices=STATUS, default='y')

    class Meta:
        verbose_name = "Menu Bar"
        verbose_name_plural = verbose_name


class Courses(models.Model):
    title = models.CharField("Tutorial name", max_length=100)
    cover = models.ImageField("Upload cover", upload_to='course', blank=True)
    category = models.CharField("Tutorial classification", max_length=100)
    introduce = models.CharField("Tutorial Introduction", max_length=200, blank=True)
    status = models.CharField("update status", max_length=50)
    article = models.ManyToManyField(Post, verbose_name="Tutorial articles", blank=True)
    created_time = models.DateTimeField('Creation time', null=True, default=timezone.now)
    # author = models.ForeignKey(User, verbose_name='作者', on_delete=models.DO_NOTHING, default="reborn")
    author = models.ForeignKey(User, verbose_name='Author', on_delete=models.DO_NOTHING)
    comments = models.PositiveIntegerField("Number of comments", default=0)
    numbers = models.PositiveIntegerField("Number of tutorials", default=0)
    views = models.PositiveIntegerField("Reading", default=0)

    class Meta:
        verbose_name = "Tutorial list"
        verbose_name_plural = verbose_name

    def get_absolute_url(self):
        return reverse('blog:course', kwargs={'pk': self.pk})


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    # subject=models.CharField(max_length=70,default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")

    # message=models.TextField()

    def __str__(self):
        return self.name
