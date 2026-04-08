def initialize_dict(student_name, subject_grades):
    return {student_name: subject_grades}

def add_student(student_grades=None):
    if student_grades is None:
        student_grades = {}
    name = input("Enter student name:\n").title()
    subjects = {}
    while True:
        entry = input("Enter subject and grade (or 'exit' to finish):\n")
        if entry.lower() == "exit":
            break
        
        parts = entry.split(",")
        subject = parts[0].strip().title()
        grade = float(parts[1].strip())
        subjects[subject] = grade
    student_grades[name] = subjects
    print(f"Student {name} successfully added to the grades management system.")
    return student_grades

def get_students(student_grades, keys):
    found_students = {}
    for search_name in keys:
        name_to_find = search_name.title()
        match_found = False
        for actual_name in student_grades.keys():
            if actual_name.lower() == search_name.lower():
                found_students[actual_name] = student_grades[actual_name]
                match_found = True
                break
        if not match_found:
            print(f"{name_to_find} not found!")
            return found_students

def avg_by_student(student_grades, keys=None):
    if keys is None:
        target_dict = student_grades
    else:
        target_dict = get_students(student_grades, keys)
        for name, subjects in target_dict.items():
            if subjects:
                grades = subjects.values()
                average = sum(grades) / len(grades)
                print(f"{name}: {average:.1f}")