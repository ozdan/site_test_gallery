# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User 
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Gallery(models.Model):
    title = models.CharField(_('Title'), max_length=255)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _('Gallery')
        verbose_name_plural = _('Galleries')


class Photo(models.Model):
    title = models.CharField(_('Title'), max_length=255)
    description = models.TextField(_('Description'), default='', blank=True)
    file = models.FileField(_('Image'), upload_to='upload/photo/%Y/%m/')
    gallery = models.ForeignKey(Gallery, null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _('Photo')
        verbose_name_plural = _('Photo')


class Comment(models.Model):
    text = models.TextField(_('Text'))
    photo = models.ForeignKey(Photo, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.text[:10]

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')