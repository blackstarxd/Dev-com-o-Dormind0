students_entrada = [
    ['Harry', 37.21],
    ['Berry', 37.21],
    ['Tina', 37.2],
    ['Akriti', 41],
    ['Harsh', 39]
]


students = []

for student in students_entrada:
    students.append({"name": student[0], "nota": student[1]})


for student in students:
    print(f"Nome: {student['name']} Nota: {student['nota']}")
    
print(sorted(students, key=lambda i: i['nota'])) #A ordem é baseada na nota.
print(sorted(students, key=lambda i: (i['nota'], i['name']))) #A ordem é baseada na nota e  na letra inicial do nome. (por isso o Berry vem antes do Harry mesmo sendo a mesma nota.)
print(sorted(students, key=lambda i: i['name'])) #A ordem é baseada na letra inicial do nome, independente da nota.