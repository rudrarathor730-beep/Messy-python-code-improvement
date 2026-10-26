
"""Improved version of the original student report program."""

SUBJECT_COUNT = 3

GRADE_A_MIN = 90
GRADE_B_MIN = 80
GRADE_C_MIN = 70
GRADE_D_MIN = 60

STUDENTS = [
    ["Rahul", 78, 88, 92],
    ["Priya", 65, 71, 69],
    ["Amit", 90, 94, 85],
    ["Sneha", 55, 60, 58],
    ["Vikram", 82, 79, 88],
]


def calculate_total_score(student_record):
    """Return the total score of a student."""
    return sum(student_record[1:])


def calculate_average_score(student_record):
    """Return the average score of a student."""
    return calculate_total_score(student_record) / SUBJECT_COUNT


def calculate_class_average(student_records):
    """Return the average of all students' average scores."""
    return sum(
        calculate_average_score(student_record)
        for student_record in student_records
    ) / len(student_records)


def count_above_class_average(student_records):
    """Return the number of students above the class average."""
    class_average = calculate_class_average(student_records)
    return sum(
        calculate_average_score(student_record) > class_average
        for student_record in student_records
    )


def assign_grade(average_score):
    """Return the grade corresponding to an average score."""
    if average_score >= GRADE_A_MIN:
        return "A"
    if average_score >= GRADE_B_MIN:
        return "B"
    if average_score >= GRADE_C_MIN:
        return "C"
    if average_score >= GRADE_D_MIN:
        return "D"
    return "F"


def find_topper(student_records):
    """Return the name and average score of the topper."""
    topper = max(student_records, key=calculate_average_score)
    return topper[0], calculate_average_score(topper)


def main():
    """Generate and display the student report."""
    print("REPORT")

    for student_record in STUDENTS:
        total_score = calculate_total_score(student_record)
        average_score = calculate_average_score(student_record)
        grade = assign_grade(average_score)

        print(f"{student_record[0]}{total_score}{average_score}{grade}")

    print(f"Class average:{calculate_class_average(STUDENTS)}")
    print(f"Above class average:{count_above_class_average(STUDENTS)}")

    topper_name, topper_average = find_topper(STUDENTS)
    print(f"Topper:{topper_name}{topper_average}")


if __name__ == "__main__":
    main()
