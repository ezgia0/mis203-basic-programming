total_score = 0
student_count = 0

while True:
    student_name = input("Enter student name (or q to quit): ")
    
    if student_name == 'q':
        break
        
    score = float(input("Enter score: "))
    
    if score < 0 or score > 100:
        print("Invalid score. Please enter a number between 0 and 100.")
        continue
        
    if score >= 90:
        letter_grade = 'A'
    elif score >= 80:
        letter_grade = 'B'
    elif score >= 70:
        letter_grade = 'C'
    elif score >= 60:
        letter_grade = 'D'
    else:
        letter_grade = 'F'
        
    print(f"{student_name}: {int(score)} -> {letter_grade}")
    
    total_score += score
    student_count += 1

if student_count > 0:
    average_score = total_score / student_count
    print(f"Total students: {student_count}")
    print(f"Average score: {average_score:.2f}")
else:
    print("No students entered.")
