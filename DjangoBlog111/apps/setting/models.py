from django.db import models
import django.utils.timezone as timezone


# Links
class FriendLinks(models.Model):
    name = models.CharField('Website name', max_length=50, default='A-Z news')
    link = models.CharField('Website address', max_length=200, default='https://www.eastnotes.com')

    class Meta:
        verbose_name = "Link"
        verbose_name_plural = verbose_name
        ordering = ['-pk']


# SEO settings
class Seo(models.Model):
    title = models.CharField("Website Master Name", max_length=100, default='DjangoEast')
    sub_title = models.CharField("Site sub title", max_length=200, default='DjangoEast')
    description = models.CharField("Website description", max_length=200, default='DjangoEast')
    keywords = models.CharField("Keyword", max_length=200, default='DjangoEast')

    class Meta:
        verbose_name = "SEO settings"
        verbose_name_plural = verbose_name


# Custom code
class CustomCode(models.Model):
    statistics = models.TextField("Website statistics code", default='Statistical code')

    class Meta:
        verbose_name = "Custom code"
        verbose_name_plural = verbose_name


# Site Information
class SiteInfo(models.Model):
    created_time = models.DateField("Station construction time", default=timezone.now)
    record_info = models.CharField("Record information", max_length=100, default='case number')
    development_info = models.CharField("Development Information", max_length=100, default='Development information')
    arrange_info = models.CharField("Deployment Information", max_length=100, default='Deployment information')

    class Meta:
        verbose_name = "Site Information"
        verbose_name_plural = verbose_name


# Social account
class Social(models.Model):
    github = models.URLField("Github address", max_length=200, default='https://github.com/zaheerkhan9800/')
    instagram = models.URLField("Instagram address", max_length=200, default='https://instagram.com/zaheerkhan9800/')
    facebook=models.URLField("Facebook address", max_length=200, default='https://www.facebook.com/profile.php?id=100008639956730')

    class Meta:
        verbose_name = "Social Accounts"
        verbose_name_plural = verbose_name
