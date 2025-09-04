def add_employee(name, emp_list=None):
    if emp_list is None:
        emp_list = []
    emp_list.append(name)
    print(emp_list)
    
all_emps = ["John", "Jane"]

add_employee("Alice")
add_employee("Bob")

print(all_emps)