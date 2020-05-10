from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from .views import ActivityViewSet, PublicActivities, PublicActivitiesDetail

router = DefaultRouter()
router.register('activities', ActivityViewSet, basename='activities')
router.register('public-activities', PublicActivitiesDetail, basename='public-activities')

custom_urlpatterns = [
    url(r'public-activities/$', PublicActivities.as_view({'get': 'list'}), name='public_activities'),
    url(r'public-activities/(?P<pk>\d+)/$', PublicActivitiesDetail.as_view({'get': 'list'}), name='public_activity_detail'),
]

urlpatterns = router.urls
urlpatterns += custom_urlpatterns
