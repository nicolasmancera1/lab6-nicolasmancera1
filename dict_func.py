# Write your code here!
def employee_print(employee_info):
    temp = employee_info.copy()
    name = temp.pop("Name", "N/A")
    print(f"Name: {name}")
    salary = temp.pop("Salary", "N/A")
    print(f"Salary: {salary}")
    role = temp.pop("Role", "N/A")
    print(f"Role: {role}")
    if not temp:
        print("No other info!")
    else:
        for key, value in temp.items():
            print(f"{key}: {value}")