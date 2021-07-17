from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from crudpractice.models import StudentData
from crudpractice.serializers import StudentDataSerializer
from rest_framework.decorators import api_view

# Create your views here.


def get_user(request):
    return HttpResponse('Hi There Mate')


@api_view(['GET', 'POST', 'DELETE'])
def student_list(request):
    if request.method == 'GET':
        students = StudentData.objects.all()

        name = request.GET.get('name', None)
        if name is not None:
            students = students.filter(name_icontains=name)

        StudentData_Serializer = StudentDataSerializer(students, many=True)
        return JsonResponse(StudentData_Serializer.data, safe=False)

    elif request.method == 'POST':
        student_data = JSONParser().parse(request)
        StudentData_Serializer = StudentDataSerializer(data=student_data)
        if StudentData_Serializer.is_valid():
            StudentData_Serializer.save()
            return JsonResponse(StudentData_Serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(StudentData_Serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'DELETE'])
def student_details(request):
    req_data = JSONParser().parse(request)
    id = req_data['id']
    try:
        student = StudentData.objects.get(id=id)
    except StudentData.DoesNotExist:
        return JsonResponse({'message': 'Student does not exists'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'POST':
        student_serializer = StudentDataSerializer(student)
        return JsonResponse(student_serializer.data)
