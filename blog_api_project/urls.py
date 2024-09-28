from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog_api_app.views import BlogViewSet

router = DefaultRouter()
router.register(r'blogs', BlogViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
