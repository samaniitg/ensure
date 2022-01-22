from django.contrib import admin
from django.urls import path, include
# for drf yasg
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Ensure assignment",
      default_version='as.1.1',
      description="Basic pis that perform CRUD operation in a todo list",
      terms_of_service="sample terms",
      contact=openapi.Contact(email="sample email"),
      license=openapi.License(name="sample license"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('api/', include('todo_list.urls')),
]
