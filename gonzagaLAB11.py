grades = []
studentNum = 1
totalGrade = 0
passedStudents = 0
loop = True

while loop == True:
    inputGrade = input(f'Student #{studentNum}: ')
    if inputGrade.isdigit():
        inputGrade = int(inputGrade)
        if inputGrade >= 40 and inputGrade <= 100:
            grades.append(inputGrade)
            studentNum += 1
        else:
            print("error should be 40-100")
    elif inputGrade.lower() == 'done':
        loop = False
    else:
        print('error input')
else:
    for grade in grades:
        totalGrade += grade
        average = totalGrade / len(grades)
    else:
        print(f'Average: {average:.2f}')

    for grade in grades:
        if grade >= 75:
            passedStudents += 1
    else:
        print(f'Number of Passed: {passedStudents}')
        percentage = (passedStudents / len(grades)) * 100
        print(f'Pass Percentage: {percentage:.2f}')