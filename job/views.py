from django.forms import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from job.models import Job
from job.serializers import JobSerializer

# def jobs_list(request):
#     jobs = Job.objects.all()
#     serializer = JobSerializer(jobs, many=True)
#     return JsonResponse(serializer.data, safe=False)

@api_view(['GET', 'POST'])
def jobs_list(request):
    jobs = Job.objects.all()
    serializer = JobSerializer(jobs, many=True)
    return Response(serializer.data)