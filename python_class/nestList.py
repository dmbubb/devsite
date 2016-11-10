students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

#sorted(student_tuples, key=lambda student: student[2])
#nested_list = [['blue', 'green'], ['red', 'black'], ['blue', 'white']]
#print(len(nested_list))
# prints 3
#print(nested_list[1])
# prints ['red', 'black']
#print(nested_list[1][0])
# prints red

minscore = []
for i in range(len(students)):
    print(students[i][1])

a = sorted(students, key=lambda student: student[1])

print(a)

unique_grades = []

for grade in 
