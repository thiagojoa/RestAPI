from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import render, get_object_or_404, redirect

from .models import Employee
from projeto.serializers import EmployeeSerializer

from django.views.generic import ListView, DetailView
from .forms import EmployeeForm

#views to make the API works
@api_view(['GET', 'POST'])
def employee_list(request):
    """
    List all employees, or create a new employee.
    """
    if request.method == 'GET':
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def employee_detail(request, pk):
    """
    Retrieve, update or delete a specific employee.
    """
    try:
        employee = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#views to make the admin front works with backend
#home view for posts. Posts are displayed in a list
class IndexView(ListView):
 template_name='app/index.html'
 context_object_name = 'employee_list'
 def get_queryset(self):
  return Employee.objects.all()

#Detail view (view employee detail)
class EmployeeDetailView(DetailView):
 model=Employee
 template_name = 'app/employee-detail.html'

#New post view (Create new employee)
def employeeview(request):
 if request.method == 'POST':
  form = EmployeeForm(request.POST)
  if form.is_valid():
   form.save()
  return redirect('index')
 form = EmployeeForm()
 return render(request,'app/employee.html',{'form': form})

#Edit a employee
def edit(request, pk, template_name='app/edit.html'):
    post= get_object_or_404(Employee, pk=pk)
    form = EmployeeForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, template_name, {'form':form})

#Delete post
def delete(request, pk, template_name='app/confirm_delete.html'):
    post= get_object_or_404(Employee, pk=pk)
    if request.method=='POST':
        post.delete()
        return redirect('index')
    return render(request, template_name, {'object':post})
