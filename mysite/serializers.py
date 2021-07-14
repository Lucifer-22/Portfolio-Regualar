from django.db.models.base import Model
from rest_framework import serializers

from .models import (Information,
                    Education,
                    Experience,
                    Skillset,
                    Message,
                    Project, 
                    User,
                    FewWords)

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class fewWordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FewWords
        fields = "__all__"

class infoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = "__all__"

class educationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = "__all__"

class experienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = "__all__"

class skillsetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skillset
        fields = "__all__"

class messageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"

class projectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


   