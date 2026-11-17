# Name: Mentari Athifa Khalish Andyni
# NIM: 2611533007
# Question 5

# BAGIAN A
username = input("Username: ")

if len(username) < 5:
    print("Invalid: at least 5 characters")
elif not username.isalnum:
    print("Invalid: letter and digits only")
elif not username[0].isalpha():
    print("Invalid: must start with a letter")
else:
    print("Valid")

# BAGIAN B
NIM = input("NIM: ")

if len(NIM) == 10 and NIM.isdigit():
    print("Valid, intake year 20" + NIM[:2])
else:
    print("Invalid NIM")