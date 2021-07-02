from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router_v1 = DefaultRouter()


router_v1.register(
    r"titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments",
    views.CommentViewSet,
    basename="comments",
)
router_v1.register(
    r"titles/(?P<title_id>\d+)/reviews",
    views.ReviewViewSet,
    basename="reviews",
)

router_v1.register(r"titles", views.TitleViewSet, basename="title")
router_v1.register(r"categories", views.CategoryViewSet, basename="category")
router_v1.register(r"genres", views.GenreViewSet, basename="genre")

urlpatterns = [path("v1/", include(router_v1.urls))]
