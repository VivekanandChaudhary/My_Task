"""My_Task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from app import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_teacher/',views.Add_teacher.as_view()), # this url Super Admin will add the teacher properties using postman and jwt tokens
    path('view_teacher/',views.View_teacher.as_view()),# this url Super Admin and teacher will see the data
    path('add_student/',views.Add_student.as_view()),# this url Super Admin will add the student properties using postman and jwt tokens
    path('view_student/',views.View_student.as_view()),# student will see the information


    path('gettoken/',TokenObtainPairView.as_view()),# user will create jwt token using postman for signup
    path('refreshtoken/',TokenRefreshView.as_view()),# user will get refresh jwt token using postman
    path('verifytoken/',TokenVerifyView.as_view()),#user will create jwt token using postman for forget password api



]
