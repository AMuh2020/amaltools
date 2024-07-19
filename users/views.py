from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, reverse, render
# Create your views here.

def login_view(request):
    if request.method == "POST":
        try:
            user = authenticate(email=request.POST["email"], password=request.POST["password"])
        except:
            return render(request, "users/login.html", {"msg_state":"your email or password is incorrect"})
        if user is not None:
            login(request, user)
            return redirect(reverse("home"))
        else:
            return render(request, "users/login.html", {"msg_state":"your email or password is incorrect"})
    else:
        return render(request, "users/login.html")

from django.contrib.auth.models import User
import csv
def temp(request):
    user_num = 0

    with open(r'/home/amaltools/amaltoolsW/amaltools_app/users/amaltools_form_password.csv', 'r') as input_file:
    
        reader = csv.reader(input_file)

        header = next(reader)

        for row in reader:
            if row[2][0:2] == '22':
                continue

            username = f"user_{user_num}"
            newUser = User.objects.create_user(username=username, password=row[3], email=row[2], first_name=row[1].split()[0])
            newUser.save()
            user_num += 1
            # print(row)
    return redirect(reverse("home"))

def logout_view(request):
    try:
        logout(request)
    except:
        pass
    
    return redirect(reverse("home"))
