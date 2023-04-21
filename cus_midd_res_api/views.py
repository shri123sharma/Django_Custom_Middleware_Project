from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import  AllowAny
from django.contrib.auth import authenticate
from rest_framework import viewsets
from django.core.mail import BadHeaderError ,send_mail
from django.http import Http404
from rest_framework.permissions import AllowAny
import json



# Create your views here.
class JobApplyView(APIView):
    permission_classes=[AllowAny]

    def get(self, request):
        query = JobApply.objects.all()
        serializer = JobApplySerializer(query,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        job_id=request.data.get('job')
        import pdb;pdb.set_trace()
        try:
            Job.objects.filter(id=job_id).exists()
            job_obj=Job.objects.get(id=job_id)
            get_job_id=job_obj.id
        except: 
            raise Response("This Job is Not Found")
        
        if get_job_id: 
            jobapply_serializer=JobApplySerializer(data=request.data)
            if jobapply_serializer.is_valid(raise_exception=True):
                jobapply_serializer.save()
                job_apply_id=JobApply.objects.filter(job_id=get_job_id).first().id
                if job_apply_id is not None:
                    if request.data.get('education'):
                        education_data=request.data.get('education')
                        education_dict_data=json.loads(education_data)  
                        education_dict_data['job_apply']=job_apply_id
                        education_serializer = EducationDetailSerilaizer(data=education_dict_data)
                        if education_serializer.is_valid(raise_exception=True):
                            education_serializer.save()

                    if request.data.get('experience'):
                        experience_data=request.data.get('experience')
                        experience_dict_data=json.loads(experience_data)
                        experience_dict_data['job_apply']=job_apply_id
                        experience_serializer = CandidateExperienceSerilaizer(data=experience_dict_data)
                        if experience_serializer.is_valid(raise_exception=True):
                            experience_serializer.save()

                
                return Response(jobapply_serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response(jobapply_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
