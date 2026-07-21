def result(marks):
    if marks >= 90:
        grade = "A+"
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 35:
        grade = "Pass"
    else:
        grade = "Fail"

    print("Grade:", grade)

result(85)
