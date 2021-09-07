from pyexpat.errors import codes

from django.db.migrations import serializer
from django.shortcuts import render
from rest_framework import viewsets, status

# Create your views here.
from rest_framework.decorators import action
from rest_framework.response import Response

from product import serializers
from product.models import Track
from product.serializers import TrackSerializer


class TrackView(viewsets.GenericViewSet):
    @action(methods=['GET'], detail=False, url_name='unit1', url_path='unit1')
    def unit_one_track(self, request, *args, **kwargs):
        qs = Track.objects.filter(unit_price__gt=1)
        qs_serializer = TrackSerializer(qs, many=True)
        return Response(data={'result': qs_serializer.data}, status=200)

    @action(methods=['GET'], detail=False, url_name='unit1', url_path='all')
    def all_track(self, request, *args, **kwargs):
        qs = Track.objects.all()
        qs_serializer = TrackSerializer(qs, many=True)
        return Response(data={'result': qs_serializer.data}, status=200)


class AlbumView(viewsets.GenericViewSet):
    @action(
        serializer_class=serializers.AlbumSerializer,
        methods=['POST'],
        detail=False,
        url_name='create_album',
        url_path='create_album'
    )
    def create_album(self, request, *args, **kwargs):
        in_serializer = serializers.AlbumSerializer(data=request.data)
        in_serializer.is_valid(raise_exception=True)
        in_serializer.save()
        return Response(
            data={
                "meta": {
                    "success": True,
                    "code": 201
                },
                "result": in_serializer.data
            },
        )
