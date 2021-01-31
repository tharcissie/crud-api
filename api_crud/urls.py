
from django.contrib import admin
from django.urls import include, path
from .views import RegisterView, CustomLoginView


# urls
urlpatterns = [
    path('', include('movies.urls')),
    path('', CustomLoginView.as_view()),
    path('rest-auth/registration/', RegisterView.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
    path('admin/', admin.site.urls),
]