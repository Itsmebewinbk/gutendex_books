from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls.static import static
from .views import index
from decouple import config


schema_view = get_schema_view(
    openapi.Info(
        title="Gutendex API",
        default_version="v1",
        description="API Documentation for Gutendex App",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="bewinbabu1998@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


url_patterns = [
    path("", index, name="index"),
    path("api/admin/", admin.site.urls),
    path("api/docs/", schema_view.with_ui("swagger", cache_timeout=0), name="docs"),
    path("api/v1/", include("books.urls")),
]


urlpatterns = url_patterns
if settings.ENVIRONMENT == "dev":
    urlpatterns = [
        path("api_gutendex/", include(url_patterns)),
    ]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    ) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
