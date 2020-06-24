from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from jobsaverapi.models import Job

class JobSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Job
        url = serializers.HyperlinkedIdentityField(
            view_name = 'job',
            lookup_field = 'id'
        )
        fields = ('id', 'company_name', 'job_title', 'notes', 'interview_date', 'user_id')
    
class Jobs(ViewSet):

    def create(self, request):
        new_job = Job()
        new_job.company_name = request.data['company_name']
        new_job.job_title = request.data['job_title']
        new_job.notes = request.data['notes']
        new_job.interview_date = request.data['interview_date']
        new_job.user_id = request.auth.user.id
        new_job.save()

        serializer = JobSerializer(new_job, context = {'request': request})

        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        try:
            job = Job.objects.get(pk=pk)
            serializer = JobSerializer(job, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        job = Job.objects.get(pk=pk)
        job.company_name = request.data['company_name']
        job.job_title = request.data['job_title']
        job.notes = request.data['notes']
        job.interview_date = request.data['interview_date']
        job.user_id = request.auth.user.id
        job.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        pass

    def list(self, request):
        jobs = Job.objects.filter(user=request.auth.user)

        company_name = self.request.query_params.get('company_name', None)
        if company_name is not None:
            jobs = Job.objects.filter(company_name__icontains=company_name)
            
        serializer = JobSerializer(
            jobs, many=True, context={'request': request}
        )
        return Response(serializer.data)
