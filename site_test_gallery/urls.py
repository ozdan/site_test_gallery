from django.conf.urls import patterns, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
MEDIA_URL = '/media/'

urlpatterns = patterns('test_gallery.views',
    url(r'^$', 'gallery_list', name='GalleryList'),
    url(r'^logout/$', 'log_out', name='LogOut'),
    url(r'^login/$', 'log_in', name='LogIn'),
    url(r'^my_gallery_list/$', 'my_gallery_list', name='MyGalleryList'),
    url(r'^create_gallery/$', 'create_gallery', name='CreateGallery'),
    url(r'^gallery/(?P<pk>\d+)/$', 'gallery', name='Gallery'),
    url(r'^my_gallery/(?P<pk>\d+)/$', 'my_gallery', name='MyGallery'),
    url(r'^create_photo/(?P<gallery_pk>\d+)/$', 'create_photo', name='CreatePhoto'),
    url(r'^update_photo/(?P<gallery_pk>\d+)/(?P<pk>\d+)/$', 'update_photo', name='UpdatePhoto'),
    url(r'^delete_photo/(?P<gallery_pk>\d+)/(?P<pk>\d+)/$', 'delete_photo', name='DeletePhoto'),
    url(r'^comments/(?P<gallery_pk>\d+)/(?P<pk>\d+)/$', 'create_comment', name='CreateComment'),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT, show_indexes=True)