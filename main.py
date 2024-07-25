import math
  
def gradingStudents(grades):
    result = []
    for i in grades:
        r = 5 * math.ceil(i / 5)
        if r - i < 3 and i >= 38:
            result.append(r)
        elif r - i >= 3 and i >= 38:
            result.append(i)
        else:
            result.append(i)
    # return result
    for i in result:
        print(i)

if __name__ == '__main__':
    grades_count = int(input().strip())
    grades = []
    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

result = gradingStudents(grades)

