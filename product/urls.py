from rest_framework import routers

from product.views import TrackView, AlbumView

router = routers.SimpleRouter()
router.register('tracks', TrackView, basename='tracks')
router.register('albums', AlbumView, basename='albums')
urlpatterns = router.urls
