from rest_framework import serializers


class ItemSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=400, allow_null=True, allow_blank=True)
    description = serializers.CharField(
        max_length=2000, allow_null=True, allow_blank=True
    )
    image = serializers.URLField(allow_null=True, allow_blank=True)
