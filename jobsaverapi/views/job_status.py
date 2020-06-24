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
        fields = ('id', 'created_at', 'job_id', 'status_id', 'job', 'status')
        depth = 1

class Job_Statuses(ViewSet):
    def create(self, request):
        new_job_status = Job_Status()
        new_job_status.job_id = request.data['job_id']
        new_job_status.status_id = request.data['status_id']
        new_job_status.created_at = request.data['created_at']
        new_job_status.save()

        serializer = JobStatusSerializer(new_job_status, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            job_status = Job_Status.objects.get(pk=pk)
            serializer = JobStatusSerializer(job_status, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        job_status = request.data['job_id']
        job_status.status_id = request.data['status_id']
        job_status.created_at = request.data['created_at']
        job_status.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        try:
            job_status = Job_Status.objects.get(pk=pk)
            job_status.delete()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except Job_Status.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        job_statuses = Job_Status.objects.all()

        serializer = JobStatusSerializer(
            job_statuses, many=True, context={'request': request}
        )
        return Response(serializer.data)