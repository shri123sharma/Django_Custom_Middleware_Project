from .models import *
from rest_framework import serializers

class CandidateDetailSerilaizer(serializers.ModelSerializer):
    class Meta:
        model=CandidateDetail
        fields='__all__'

class JobApplySerializer(serializers.ModelSerializer):
    class Meta:
        model=JobApply
        fields='__all__'

class CandidateExperienceSerilaizer(serializers.ModelSerializer):
    class Meta:
        model=CandidateExperience
        fields='__all__'

class EducationDetailSerilaizer(serializers.ModelSerializer):
    class Meta:
        model=EducationDetail
        fields='__all__'

