
PASS_SCORE = 65
student_3007 = int(input("Number of Student: "))

while student_3007 < 1:
    print("Invalid student count!")
    student_3007 = int(input("Number of Student: "))

lowest_3007 = 100
lulus_3007 = 0
total_3007 = 0

for i in range(student_3007):
    nilai_3007 = int(input("Enter score: "))
    while nilai_3007 < 0 or nilai_3007 > 100:
        print("Invalid score!")
        nilai_3007 = int(input("Enter score: "))
    if nilai_3007 >= PASS_SCORE:
        lulus_3007 += 1
    if nilai_3007 < lowest_3007:
        lowest_3007 = nilai_3007
    total_3007 += nilai_3007

average_3007 = round(total_3007 / student_3007, 2)

print("Total score:", total_3007)
print("Average score:", average_3007)
print("Passed students:", lulus_3007)
print("Lowest score:", lowest_3007)