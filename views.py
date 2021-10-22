from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListAPIView
from app.models import Student,Teacher

from app.serializers import StudentSerializer,TeacherSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated



class Add_teacher(CreateAPIView):
    queryset = Teacher.objects.all() # This Queryset is adding the Teacher and return dict data
    serializer_class = TeacherSerializer # serializer class  will converting dict data to json data


class View_teacher(ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class Add_student(CreateAPIView):
    queryset = Student.objects.all()# This Queryset is adding the student and return dict data
    serializer_class = StudentSerializer # serializer class  will converting dict data to json data

class View_student(ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
