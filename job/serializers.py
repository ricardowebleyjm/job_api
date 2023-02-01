from rest_framework import serializers
from job.models import Job, Category

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields ="__all__"