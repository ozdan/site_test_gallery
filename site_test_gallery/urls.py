from django.conf.urls import patterns, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('test_gallery.views',
    url(r'^$', 'gallery_list', name='GalleryList'),
    url(r'^logout/$', 'log_out', name='LogOut'),
    url(r'^login/$', 'log_in', name='LogIn'),
    url(r'^my_gallery_list/$', 'my_gallery_list', name='MyGalleryList'),
    url(r'^create_gallery/$', 'create_gallery', name='CreateGallery'),
    url(r'^gallery/(?P<pk>\d+)/$', 'gallery', name='Gallery'),
    url(r'^create_photo/(?P<gallery_pk>\d+)/$', 'create_photo', name='CreatePhoto'),
    url(r'^update_photo/(?P<gallery_pk>\d+)/(?P<pk>\d+)/$', 'update_photo', name='UpdatePhoto'),
)
# 
# 
# urlpatterns += patterns('',
#     url(r'^login/$', login,
#         {
#             'template_name': 'test_gallery/login.html',
#             'redirect_field_name': reverse('GalleryList')
#         },
#         name='LogIn'
#     ),
# )