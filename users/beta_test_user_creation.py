import csv
from django.conf import settings
settings.configure()
from django.contrib.auth.models import User

user_num = 0

with open(r'/home/amaltools/amaltoolsW/amaltools_app/users/amaltools_form_password.csv', 'r') as input_file:
   
    reader = csv.reader(input_file)

    header = next(reader)

    for row in reader:
        if row[2][0:2] == '22':
            continue

        username = f"user_{user_num}"
        # newUser = User.objects.create_user(username=username, password=row[3], email=row[2], first_name=row[1].split()[0])
        # newUser.save()
        user_num += 1
        print(row)