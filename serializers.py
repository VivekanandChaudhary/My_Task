from rest_framework.serializers import ModelSerializer
from app.models import Teacher,Student

class TeacherSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"

class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
