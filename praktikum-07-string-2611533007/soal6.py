# Name: Mentari Athifa Khalish Andyni
# NIM: 2611533007
# Question 6

first_name = " muhammad"
last_name = "rafi "
full_name = first_name.strip() + " " + last_name.strip()
print(full_name)
print(full_name.title())

full_name = "  Siti Aisyah  "
nim = "2610511023"
clean_name = full_name.strip()
space = clean_name.find(" ")

if space == -1:
    first_name = clean_name
else:
    first_name = clean_name[:space]
username = first_name.lower() + nim[-3:]
print(username)

full_name = "Muhammad Rafi Pratama"
nim = "2610511045"
clean_name = full_name.strip()
space = clean_name.find(" ")

if space == -1:
    first_name = clean_name
else:
    first_name = clean_name[:space]
username = first_name.lower() + nim[-3:]
print(username)

full_name = "Kartika"
nim = "2610511007"
clean_name = full_name.strip()
space = clean_name.find(" ")

if space == -1:
    first_name = clean_name
else:
    first_name = clean_name[:space]
username = first_name.lower() + nim[-3:]
print(username)

full_name = "Mentari Athifa Khalish Andyni"
nim = "2611533007"
clean_name = full_name.strip()
space = clean_name.find(" ")

if space == -1:
    first_name = clean_name
else:
    first_name = clean_name[:space]
username = first_name.lower() + nim[-3:]
print(username)