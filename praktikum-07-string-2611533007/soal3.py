# Name: Mentari Athifa Khalish Andyni
# NIM: 2611533007
# Question 3

# BAGIAN A
text = "Informatika"
print(text[10])
print(text.upper())
print(text[0:20])

# BAGIAN B
text = "Mentari Athifa Khalish Andyni"
text = text.lower()
count = 0
for char in text:
    if char in "aiueo":
        count = count + 1
print("Vowels:", count)