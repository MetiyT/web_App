from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserSignupForm
from .models import  Employee,Attendance
from django.utils import timezone 
from datetime import timedelta
from datetime import timedelta

def signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = UserSignupForm()
    return render(request, 'signup.html', {'form': form})
def signout(request):
    logout(request)
    return redirect('login')

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            user.save()
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

from .models import Employee

def home(request):
    employee_code = None
    attendance = None
    attendance_records = None
    total_working_hours_daily= None
    total_working_hours_weekly = None
    total_working_hours_monthly= None

    if request.user.is_authenticated:
        employee = Employee.objects.filter(user=request.user).first()

        if employee is None:
            # Create a new Employee object for the user with a generated employee code
            employee_code = generate_employee_code()
            employee = Employee.objects.create(user=request.user, employee_code=employee_code)
        else:
            employee_code = employee.employee_code

        # Retrieve or create the attendance object
        attendance, created = Attendance.objects.get_or_create(employee=employee, check_out=None)

        # Attendance logic
        if request.method == 'POST':
            if attendance.check_in:
                # Employee is checking out
                attendance.check_out = timezone.now()
                attendance.save()
            else:
                # Employee is checking in
                attendance.check_in = timezone.now()
                attendance.save()
        attendance_records = Attendance.objects.filter(employee=employee)
        total_working_hours_daily = calculate_total_working_hours(attendance_records, 'day')
        total_working_hours_weekly = calculate_total_working_hours(attendance_records, 'week')
        total_working_hours_monthly = calculate_total_working_hours(attendance_records, 'month')

    context = {
        'employee_code': employee_code,
        'attendance': attendance,
        'attendance_records': attendance_records,
        'total_working_hours_daily': total_working_hours_daily,
        'total_working_hours_weekly': total_working_hours_weekly,
        'total_working_hours_monthly': total_working_hours_monthly,
    }
    return render(request, 'home.html', context)


def calculate_total_working_hours(attendance_records, period):
    total_working_hours = timedelta()

    # Filter attendance records based on the period
    if period == 'day':
        filtered_records = attendance_records.filter(check_in__date=timezone.now().date())
    elif period == 'week':
        filtered_records = attendance_records.filter(check_in__week=timezone.now().isocalendar()[1])
    elif period == 'month':
        filtered_records = attendance_records.filter(check_in__month=timezone.now().month)
    else:
        return total_working_hours

    # Calculate the total working hours for the filtered records
    for record in filtered_records:
        if record.check_in and record.check_out:
            working_hours = record.check_out - record.check_in
            total_working_hours += working_hours

    return total_working_hours
def generate_employee_code():
    last_employee = Employee.objects.order_by('-id').first()
    last_employee_code = last_employee.employee_code if last_employee else None
    
    if last_employee_code and last_employee_code.startswith('EMP-'):
        try:
            code = int(last_employee_code.split('-')[1])
            new_code = code + 1
            employee_code = f'EMP-{new_code:03}'
        except (ValueError, IndexError):
            employee_code = 'EMP-001'
    else:
        employee_code = 'EMP-001'
    
    return employee_code