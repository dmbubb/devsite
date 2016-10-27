
#N = int(input())
N = 2
    
students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
stu = sorted(students, key=lambda student: student[1]) 
print(stu)
min_g = stu[0][1]
sec_worst = []
for i in range(len(stu)):
    if stu[i][1] > min_g:
        sec_worst.append(stu[i][1])

    print(sec_worst)
        
