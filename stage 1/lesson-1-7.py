grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# тут можно было бы в рамках текущих знаний поступить в лоб
# grades[0] = sum(grades[0])/len(grades[0])
# grades[1] = sum(grades[1])/len(grades[1])
# grades[2] = sum(grades[3])/len(grades[2])
# grades[3] = sum(grades[3])/len(grades[3])
# grades[4] = sum(grades[4])/len(grades[4])

#Но цикл прям так и напрашивается тут ^^^
avg_grades = list()
for val in grades:
    avg_grades.append(sum(val)/len(val))


students_grades = dict(zip(students,avg_grades))
# print(students_grades)
# ^^^ Можно было бы вывести и так. Но хочется чуть красивее

for key,val in students_grades.items():
    print(f"{key} avarage grade is {val}")

