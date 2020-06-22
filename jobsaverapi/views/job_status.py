from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from ..models import Job_Status

class JobStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Job_Status
        url = serializers.HyperlinkedIdentityField(
            view_name = 'job_status',
            lookup_field = 'id'
        )
        fields = ('id', 'created_at', 'job_id', 'status_id')
        depth = 2

class Job_Statuses(ViewSet):
    def list(self, request):
        job_statuses = Job_Status.objects.all()

        serializer = JobStatusSerializer(
            job_statuses, many=True, context={'request': request}
        )
        return Response(serializer.data)