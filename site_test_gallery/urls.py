from django.conf.urls import patterns, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('test_gallery.views',
    url(r'^$', 'gallery_list', name='GalleryList'),
    url(r'^logout/$', 'log_out', name='LogOut'),
    url(r'^login/$', 'log_in', name='LogIn'),
    url(r'^my_gallery_list/$', 'gallery_list', name='MyGalleryList'),
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