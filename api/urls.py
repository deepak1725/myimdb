from django.conf.urls import url, include
from api import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

# from rest_auth.registration.views import RegisterView, VerifyEmailView
# from django.views.generic import TemplateView

app_name = "api"

router = DefaultRouter()
router.register(r'movies', views.MoviesViewSet, base_name="movies")

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^loaddata', views.LoadDataView.as_view(), name='register'),
    url(r'^', views.HomePageView.as_view(), name='home'),
]