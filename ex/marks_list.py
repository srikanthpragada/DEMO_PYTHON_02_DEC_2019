students = {}
data = ["abc,93,33,22", "xyz,73,55,66", "pqr,88,44,55,55"]

for line in data:
    parts = line.split(",")
    # convert all elements from str to int
    for i in range(1,len(parts)):
        parts[i] = int(parts[i])

    students[parts[0]] = parts[1:]


for name, marks in sorted(students.items()):
    total = sum(marks)
    print(f"{name:10} {str(marks).strip('[]'):20} {total}  {total / len(marks):0.2f}")

