from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
]


# *************Language preference***********

# from django.contrib import admin
# from django.urls import include, path
# from django.conf.urls.i18n import i18n_patterns 

# urlpatterns = i18n_patterns(
#         path('', include('pages.urls')),
#         path('admin/', admin.site.urls),
#         prefix_default_language=False,
#     )          