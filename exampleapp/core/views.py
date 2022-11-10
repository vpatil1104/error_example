#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import EmployeeForm

def admin_vali(request):
    if request.method == "POST":  
        form = EmployeeForm(request.POST)
        if form.is_valid():
            print('Employee Id:', form.cleaned_data['emp_id'])
            print('Employee Name:', form.cleaned_data['name'])            
            print('Assignment Assign:', form.cleaned_data['assignment_assign']) 
            print('Start Date:', form.cleaned_data['start_date'])
            print('End Date:', form.cleaned_data['end_date'])
            form.save()
                        
    else:
        form =EmployeeForm()
    
    return render(request,'form.html',{'form':form})