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
        instance.user = self.request.user
        instance.save(commit)
        return instance


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('title', 'description', 'file',)

    def __init__(self, gallery_pk, *args, **kwargs):
        super(PhotoForm, self).__init__(*args, **kwargs)
        self.gallery_pk = gallery_pk

    def save(self, commit=True):
        instance = super(PhotoForm, self).save(commit=False)
        if instance.pk:
            instance.save()
        else:
            instance.gallery_id = self.gallery_pk
            instance.save()
        return instance


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
