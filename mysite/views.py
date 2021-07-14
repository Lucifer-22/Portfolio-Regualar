from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import (Information,
                    Education,
                    Experience,
                    Skillset,
                    Message,
                    Project,
                    User,
                    FewWords)

from .serializers import (  infoSerializer,
                            educationSerializer,
                            experienceSerializer,
                            skillsetSerializer,
                            messageSerializer,
                            projectSerializer,
                            userSerializer,
                            fewWordsSerializer)
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework import permissions, serializers

# Create your views here.
@api_view(['GET'])
@permission_classes((permissions.AllowAny, permissions.IsAuthenticated))
def bio_view(request, username, *args, **kwargs):
    bioProfile = User.objects.get(username = username)  
    information = Information.objects.filter(user = bioProfile).first()
    education = Education.objects.filter(user = bioProfile).all()
    experience = Experience.objects.filter(user = bioProfile).all().order_by('-id')
    skillset = Skillset.objects.filter(user = bioProfile).all().order_by('-id')
    project = Project.objects.filter(user = bioProfile).all().order_by('-id')
    few_words = FewWords.objects.filter(user = bioProfile).all()

    usernameSerializer = userSerializer(bioProfile, many=False)
    informationSerializer = infoSerializer(information, many = False)
    eduSerializer = educationSerializer(education, many= True)
    expSerializer = experienceSerializer(experience, many = True)
    skillSerializer = skillsetSerializer(skillset, many = True)
    projSerializer = projectSerializer(project, many = True)
    fewWordSerializer = fewWordsSerializer(few_words, many = True)
    context = {
        "bioprofile": usernameSerializer.data,
        "information": informationSerializer.data,
        "education": eduSerializer.data,
        "experience": expSerializer.data,
        "skillset": skillSerializer.data,
        "project": projSerializer.data,
        "fewWords": fewWordSerializer.data, 
    }
    return Response(context)


def index(request, *args, **kwargs):
    return render(request, template_name="mysite/index.html")

def getUserInfo(request, *args, **kwargs):
    user = request.user
    currentUserName = request.user.username
    if not user.is_authenticated:
        # Do something for anonymous users
        user = "Admin"
        currentUserName = "Admin"
    
    context= {"username":currentUserName}
    return JsonResponse(context, safe= False)
