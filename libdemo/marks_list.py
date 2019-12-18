
students = []

with open("marks.txt") as f:
    for line in f.readlines():
        parts = line.split(",")
        if len(parts) < 2:
            continue

        name = parts[0]
        sum = 0
        count = 0
        for m in parts[1:]:
            try:
                sum += int(m)
                count += 1
            except:
                pass

        if count == 0:
            continue

        avg = sum / count
        students.append( (name,sum,avg))


for name,total,avg in sorted(students):
    print(f"{name:20} {total:5d} {avg:.2f}")


