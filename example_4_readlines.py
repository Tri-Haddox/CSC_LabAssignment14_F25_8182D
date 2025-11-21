file_obj = open("data1.txt", "r")
lines = file_obj.readlines()

print(len(lines))

line_no = 1
for line in lines:
    print(f"Line {line_no}: {line}")
    line_no += 1 