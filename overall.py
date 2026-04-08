def student_averages(students):
    result = {}
    for student_id, assignments in students.items():
        grades = assignments.values()
        average = round(sum(grades) / len(grades))
        result[student_id] = average
    return result

def assignment_averages(students):
    totals = {}
    counts = {}
    for student_id, assignments in students.items():
        for task, grade in assignments.items():
            if task not in totals:
                totals[task] = 0
                counts[task] = 0
            totals[task] += grade
            counts[task] += 1
            result = {}
    for task in totals:
        result[task] = round(totals[task] / counts[task])
    return result