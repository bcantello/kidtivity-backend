from rest_framework import generics, viewsets
from rest_framework.exceptions import ValidationError, PermissionDenied
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Activity
from .serializers import ActivitySerializer


class ActivityViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Activity.objects.all().filter(owner=self.request.user)
        return queryset

    serializer_class = ActivitySerializer

    def create(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            raise PermissionDenied("You must be logged in to create a activity")
        return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        activity = Activity.objects.get(pk=self.kwargs["pk"])
        if not request.user == activity.owner:
            raise PermissionDenied("Only the author may delete this activity")
        return super().destroy(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        activity = Activity.objects.get(pk=self.kwargs["pk"])
        if not request.user == activity.owner:
            raise PermissionDenied("Only the author may edit this activity")
        return super().update(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PublicActivity(generics.ListAPIView):
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = Activity.objects.all().filter(is_public=True)
        return queryset

    serializer_class = ActivitySerializer


class PublicActivityDetail(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = Activity.objects.all().filter(is_public=True)
        return queryset

    serializer_class = ActivitySerializer
