# Create your views here.

from django.http import Http404

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import ItemSerializer
from .tasks import get_all_items_from_cache, get_single_item


class ItemList(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "result_count",
                openapi.IN_QUERY,
                description="Number of results per page",
                type=openapi.TYPE_STRING,
            ),
            openapi.Parameter(
                "offset",
                openapi.IN_QUERY,
                description="Page number to get",
                type=openapi.TYPE_STRING,
            ),
        ]
    )
    def get(self, request, format=None):
        result_count = int(request.GET.get("result_count", 20))
        offset = int(request.GET.get("offset", 0))

        items, total = get_all_items_from_cache(result_count, offset)

        return Response(
            {"items": ItemSerializer(items, many=True).data, "total": total},
            status=status.HTTP_200_OK,
        )


class ItemDetail(APIView):
    def get(self, request, id, format=None):
        item = get_single_item(id)
        if not hasattr(item, "title"):
            raise Http404
        return Response(ItemSerializer(item).data, status=status.HTTP_200_OK)
