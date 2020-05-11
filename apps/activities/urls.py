from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from .views import ActivityViewSet, PublicActivities, PublicActivitiesDetail

router = DefaultRouter()
router.register('activities', ActivityViewSet, basename='activities')

custom_urlpatterns = [
    url(r'^public-activities/$', PublicActivities.as_view(), name='public-activities'),
    url(r'^public-activities/(?P<pk>\d+)/$', PublicActivitiesDetail.as_view(), name='public-activity-detail'),
]

urlpatterns = router.urls
urlpatterns += custom_urlpatterns
