import os
import csv 

os.chdir("C:/Users/dy/Default/ansel/Desktop/dy/1.computer_science/cs_knowledge/python/04.IT_automation_with_python/02.os_operation_system/reading_and_writing_csv_files")
print(os.getcwd())
f = open("data.csv")
csv.reader(f)
csv_f = csv.reader(f)
i = -1
for row in csv_f:
    name, sex, age, address = row
    i = i + 1
    if (i == 0):
        continue
    print(f"Name: {name}, Sex: {sex}, Age: {age}, Address: {address}")
f.close()