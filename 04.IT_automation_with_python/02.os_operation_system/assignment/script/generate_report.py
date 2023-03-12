import csv
import os

def read_employees(csv_file_location):
    # other way of opening csv file (linux)
    # csv.register_dialect("empDialect", skipinitialspace=True, strict=True)
    # employee_file = csv.DictReader(open(csv_file_location), dialect="empDialect")
    
    # conservitive method
    file_dir = csv_file_location + "./employees.csv"
    employee_list = []
    with open(file_dir, "r") as f:
        rows = csv.DictReader(f)
        for row in rows:
            print(row)
            employee_list.append(row)
    return (employee_list)

def process_data(employee_list):
    department_list = []
    for employee_data in employee_list:
        department_list.append(employee_data[" Department"])

    department_data = {}    
    for department_name in set(department_list): # set data type is used to remove duplicates
        department_data[department_name] = department_list.count(department_name)
    return (department_data)

def write_report(dictionary, report_file):
    with open(report_file, "w+") as f:
        res = ""
        for data in sorted(dictionary):
            res = str(data[1:]) + " : " + str(dictionary[data]) + "\n"
            f.write(res)
        f.close()

def main():
    os.chdir("C:/Users/dy/Default/ansel/Desktop/dy/1.computer_science/cs_knowledge/python/04.IT_automation_with_python/02.os_operation_system/assignment/data")
    csv_file_location = os.getcwd()
    print("--------------------------------------------\n")
    print(csv_file_location)
    print("\n")
    employee_list = read_employees(csv_file_location)
    print("\n\n", employee_list, "\n\n")
    dictionary = process_data(employee_list)
    print(dictionary)
    report_file = "C:/Users/dy/Default/ansel/Desktop/dy/1.computer_science/cs_knowledge/python/04.IT_automation_with_python/02.os_operation_system/assignment/output/report.txt"
    write_report(dictionary, report_file)

    
    
if __name__ == main():
    main()
    