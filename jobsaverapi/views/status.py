from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
# from rest_framework import status
from ..models import Status

class StatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Status
        url = serializers.HyperlinkedIdentityField(
            view_name = 'status',
            lookup_field = 'id'
        )
        fields = ('id', 'name')

class Statuses(ViewSet):
    def retrieve(self, request, pk=None):
        try:
            status = Status.objects.get(pk=pk)
            serializer = StatusSerializer(
                status, context={'request': request}
            )
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        statuses = Status.objects.all()

        serializer = StatusSerializer(
            statuses, many=True, context={'request': request}
        )
        return Response(serializer.data)