# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from .models import Photo, Gallery, Comment


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('title', 'description', 'file',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
