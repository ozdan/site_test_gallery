# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from .models import Photo, Gallery, Comment


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ('title',)

    def __init__(self, request, *args, **kwargs):
        super(GalleryForm, self).__init__(*args, **kwargs)
        self.request = request

    def save(self, commit=True):
        instance = super(GalleryForm, self).save(commit=False)
        if not instance.pk:
            instance.user = self.request.user
        instance.save(commit)
        return instance


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('title', 'description', 'file',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
