# Name: Mentari Athifa Khalish Andyni
# NIM: 2611533007
# Question 7

print("=" * 30)
print("STUDENT CARD")
print("=" * 30)

Name = "Mentari Athifa Khalish Andyni"
NIM = "2611533007"
Username = Name.strip().lower()[:8] + NIM[-3:]
Intake = "20" + NIM[:2]

print("=" * 30)
print("STUDENT CARD".center(30))
print("=" * 30)
print(f"{'Name':10}" + ": ", Name.title())
print(f"{'NIM':10}" + ": ", NIM)
print(f"{'Username':10}" + ": ", Username)
print(f"{'Intake':10}" + ": ", Intake)
print("=" * 30)
