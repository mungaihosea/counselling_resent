from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login as login_user, logout as logout_user
from django.shortcuts import redirect, get_object_or_404
from .models import Appointment

def login(request):
    error = None
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, password)
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                login_user(request, user)
                return redirect('dash')
            else:
                error = "invalid login credentials"
                return render(request, 'login.html', {"error": error})
        except:
            return render(request, 'login.html', {"error": error})

    return render(request, 'login.html', {"error": error})

def dash(request):
    if request.user.is_authenticated == False:
        return redirect('login')
    students = User.objects.filter(is_superuser = False)
    my_appointments = Appointment.objects.filter(user = request.user)
    context = {
        "students":students,
        "my_appointments":my_appointments,
        "all_appointments":Appointment.objects.all(),
     }
    return render(request, 'dash.html', context)

def register(request):
    error = None
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        re_password = request.POST.get("re_password")
        email = request.POST.get("email")
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        if password != re_password:
            return render(request, 'register.html', {})

        try:
            # create new user 
            new_user = User()
            new_user.username = username
            new_user.first_name = first_name
            new_user.last_name = last_name
            new_user.email = email
            new_user.set_password(password)
            new_user.save()
            print('user created successfully ')
        except:
            error = "an error occured"
            return render(request, 'register.html', {"error": error})

        #login user and redirect to dashboard
        login_user(request, new_user)
        return redirect('dash')

    return render(request, 'register.html', {"error": error})

def create_appointment(request):
    if request.user.is_superuser == False:
        return redirect('login')

    if request.method == "POST":
        try:
            username = request.POST.get('student')
            user = User.objects.get(username = username)
        except:
            return redirect('dash')
        date = request.POST.get("date")
        counsellor = request.POST.get("counsellor")
        subject = request.POST.get('subject')
    
        #create appointment
        ap = Appointment()
        ap.user = user
        ap.date = date
        ap.subject = subject
        ap.counsellor = counsellor
        ap.save()

        return redirect('dash')
    return redirect('dash')

def about(request):
    return render(request, 'about.html', {})

def update_profile(request):
    return render(request, 'update_profile.html', {})

def logout(request):
    logout_user(request)
    return redirect('login')

def cancel_appointment(request, id):
    ap = get_object_or_404(Appointment, id = id)
    ap.delete()
    return redirect('dash')