from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from rest_framework import urls as drf_urls
from rest_framework.documentation import include_docs_urls

from apps.common.api.v1.views import SignS3

api_patterns = [
    path('v1/sign-s3', SignS3.as_view(), name='sign_s3'),
]

urlpatterns = [
    # Django
    path('admin/', admin.site.urls),

    # DRF
    path('api-auth/', include(drf_urls)),
    path('api/docs/', include_docs_urls(title='Holo Apollo API', public=False)),
    path('api/', include(api_patterns)),

    # Apps
]

if settings.ENABLE_DDT:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
