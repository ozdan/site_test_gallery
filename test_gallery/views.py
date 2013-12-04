# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import logout
from django.contrib.auth.views import login
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy, reverse
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


class MyGalleryListView(ListView):
    model = Gallery
    template_name = 'test_gallery/my_gallery_list.html'

    def get_queryset(self):
        qs = super(MyGalleryListView, self).get_queryset()
        return qs.filter(user_id=self.request.user.pk)

my_gallery_list = login_required(MyGalleryListView.as_view())


class CreateGalleryView(CreateView):
    model = Gallery
    form_class = GalleryForm
    template_name = 'test_gallery/create_gallery.html'
    success_url = reverse_lazy('MyGalleryList')

    def get_form_kwargs(self):
        kwargs = super(CreateGalleryView, self).get_form_kwargs()
        kwargs.update({
            'request': self.request,
        })
        return kwargs

create_gallery = login_required(CreateGalleryView.as_view())


class PhotoListView(ListView):
    model = Photo
    template_name = 'test_gallery/gallery.html'

    def get_context_data(self, **kwargs):
        context = super(PhotoListView, self).get_context_data(**kwargs)
        context['gallery_pk'] = self.kwargs['pk']
        return context

    def get_queryset(self):
        qs = super(PhotoListView, self).get_queryset()
        return qs.filter(gallery=self.kwargs['pk'])

gallery = PhotoListView.as_view()


class MyPhotoListView(PhotoListView):
    model = Photo
    template_name = 'test_gallery/my_gallery.html'

my_gallery = login_required(MyPhotoListView.as_view())


class CreateUpdateFormMixin(object):
    form_class = PhotoForm
    model = Photo
    
    def get_success_url(self):
        return reverse_lazy('MyGallery', kwargs={'pk': self.kwargs['gallery_pk']})
    
    def get_form_kwargs(self):
        kwargs = super(CreateUpdateFormMixin, self).get_form_kwargs()
        kwargs.update({
            'gallery_pk': self.kwargs['gallery_pk']
        })
        return kwargs


class CreatePhotoView(CreateUpdateFormMixin, CreateView):
    template_name = 'test_gallery/create_photo.html'

create_photo = login_required(CreatePhotoView.as_view())


class UpdatePhotoView(CreateUpdateFormMixin, UpdateView):
    template_name = 'test_gallery/update_photo.html'

update_photo = login_required(UpdatePhotoView.as_view())


class DeletePhotoView(DeleteView):
    model = Photo
    template_name = 'test_gallery/delete_photo.html'

    def get_success_url(self):
        return reverse_lazy('MyGallery', kwargs={'pk': self.kwargs['gallery_pk']})

    def get_context_data(self, **kwargs):
        context = super(DeletePhotoView, self).get_context_data(**kwargs)
        context['gallery_pk'] = self.kwargs['pk']
        return context

delete_photo = login_required(DeletePhotoView.as_view())


class CreateCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'test_gallery/create_comment.html'

    def get_form_kwargs(self):
        kwargs = super(CreateCommentView, self).get_form_kwargs()
        kwargs.update({
            'request': self.request,
            'photo_pk': self.kwargs['pk']
        })
        return kwargs

    def get_success_url(self):
            return reverse_lazy(
                'CreateComment',
                kwargs={
                    'gallery_pk': self.kwargs['gallery_pk'],
                    'pk': self.kwargs['pk']
                }
            )

    def get_context_data(self, **kwargs):
        context = super(CreateCommentView, self).get_context_data(**kwargs)
        context['comment_list'] = Comment.objects.filter(photo_id=self.kwargs['pk'])
        return context

create_comment = login_required(CreateCommentView.as_view())
