from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
# Create your views here.

# get single student data - model object
def student_detail(request,pk):
    stu = Student.objects.get(id=pk)
    # print(stu)
    serialzer = StudentSerializer(stu)
    # print(serialzer.data)

    # json_data = JSONRenderer().render(serialzer.data)
    # print(json_data)
    # return HttpResponse(json_data,content_type='application/json')

    return JsonResponse(serialzer.data,safe=False)

# get all student data - Query set
def student_list(request):
    stu = Student.objects.all()
    # print(stu)
    serialzer = StudentSerializer(stu,many=True)
    # print(serialzer.data)
    # json_data = JSONRenderer().render(serialzer.data)
    # # print(json_data)
    # return HttpResponse(json_data,content_type='application/json')
    
    return JsonResponse(serialzer.data,safe=False)