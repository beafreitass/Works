def getLetterGrade(average) :
    if average >= 90 :
        return "A"
    elif average >= 80 :
        return "B"
    elif average >= 70 :
        return "C"
    elif average >= 60 :
        return "D"
    else :
        return "F"

name = input("Student name: ")

grades = []
grades.append(float(input("Grade 1: ")))
grades.append(float(input("Grade 2: ")))
grades.append(float(input("Grade 3: ")))
grades.append(float(input("Grade 4: ")))
grades.append(float(input("Grade 5: ")))

average = sum(grades) / len(grades)

print(name)
print("Average:", format(average, "g"))
print("Letter Grade:", getLetterGrade(average))