# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import logout
from django.contrib.auth.views import login
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import GalleryForm, PhotoForm, CommentForm
from .models import Gallery, Photo, Comment


def log_in(request):
    return login(request, template_name='test_gallery/login.html')


def log_out(request):
    logout(request)
    return redirect(reverse('GalleryList'))


class GalleryListView(ListView):
    model = Gallery
    template_name = 'test_gallery/gallery_list.html'

gallery_list = GalleryListView.as_view()


class CreateGalleryView(CreateView):
    model = Gallery
    form_class = GalleryForm
    template_name = 'test_gallery/create_gallery.html'

create_gallery = login_required(CreateGalleryView.as_view())


class CreateUpdateFormMixin(object):
    form_class = PhotoForm
    model = Photo


class CreatePhotoView(CreateView, CreateUpdateFormMixin):
    template_name = 'test_gallery/create_photo.html'

create_photo = login_required(CreatePhotoView.as_view())


class UpdatePhotoView(UpdateView, CreateUpdateFormMixin):
    template_name = 'test_gallery/update_photo.html'

update_photo = login_required(UpdatePhotoView.as_view())


class DeletePhotoView(DeleteView):
    model = Photo
    template_name = 'test_gallery/delete_photo.html'

delete_photo = login_required(DeletePhotoView.as_view())


class CreateCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'test_gallery/create_comment.html'

create_comment = login_required(CreateCommentView.as_view())
