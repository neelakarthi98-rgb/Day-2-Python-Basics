student_grades = {
    "Alice": [88, 92, 78],
    "Bob": [75, 80, 85],
    "Charlie": [95, 89, 90]
}
highest_score=-1
lowest_score=101
for student, grades in student_grades.items():
    
    # Calculate the average grade for the current student
    average = sum(grades) / len(grades)
    print(f"{student}'s average grade is: {average:.2f}")

    #find the highest and lowest score for the current student

    for grade in grades:
        if grade>highest_score:
            highest_score=grade
        if grade<lowest_score:
            lowest_score=grade
print(f"The hightest score recorded is: {highest_score}")
print(f"The lowest score recorded is: {lowest_score}")