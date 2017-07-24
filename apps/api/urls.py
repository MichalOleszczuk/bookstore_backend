from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, CheckAuthView
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('books', BookViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^token-auth/', obtain_auth_token),
    url(r'^check-auth/', CheckAuthView.as_view()),
]
