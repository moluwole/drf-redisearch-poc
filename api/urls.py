from django.urls import path

from .views import ItemDetail, ItemList

urlpatterns = [path("", ItemList.as_view()), path("<int:id>", ItemDetail.as_view())]
