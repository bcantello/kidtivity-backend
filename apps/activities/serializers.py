from rest_framework import serializers
from .models import Activity


class ActivitySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Activity
        fields = (
            'id',
            'title',
            'owner',
            'category',
            'age_range',
            'summary',
            'supplies',
            'body',
            'image',
            'created_at',
            'updates_at',
            'is_public',
        )
