# Домашнее задание по уроку 1.5
# «Практика по использованию циклов, коллекций и функций»
# Выполнил Мартысюк Илья PY-3

students = [
    {'name': 'Василий', 'surname': 'Пупкин', 'sex': 'm', 'experience': True, \
    'evaluation': (9, 7, 4, 2, 7), 'exam': 9},
    {'name': 'Евгений', 'surname': 'Смернов', 'sex': 'm', 'experience': True, \
    'evaluation': (10, 10, 9, 3, 7), 'exam': 10},
    {'name': 'Петр', 'surname': 'Смернов', 'sex': 'm', 'experience': False, \
    'evaluation': (4, 2, 6, 1, 9), 'exam': 7},
    {'name': 'Дмитрий', 'surname': 'Давыдов', 'sex': 'm', 'experience': False, \
    'evaluation': (4, 4, 4, 4, 4), 'exam': 2},
    {'name': 'Татьяна', 'surname': 'Брамс', 'sex': 'f', 'experience': True, \
    'evaluation': (7, 9, 3, 10, 10), 'exam': 10},
    {'name': 'Мария', 'surname': 'Крынкина', 'sex': 'f', 'experience': False, \
    'evaluation': (9, 8, 9, 5, 2), 'exam': 5}
  ]

countOfStudents = len(students)
countOfEvaluations = len(students[0]['evaluation'])

def averageEvaluations():
    countOfAllEvaluation = 0
    countOfAllExam = 0

    for student in students:
        countOfAllEvaluation += sum(student['evaluation'])
        countOfAllExam += student['exam']

    countOfAllEvaluation = round(countOfAllEvaluation / (countOfStudents * countOfEvaluations), 1)
    countOfAllExam = round(countOfAllExam / countOfStudents, 1)
    return countOfAllEvaluation, countOfAllExam

def averageRatingsCount(whatCount, value):
    countEvaluations = 0
    countExams = 0
    countFilteredStudents = 0

    for student in students:
        if whatCount == 'sex':
            if student['sex'] == value == 'm':
                countEvaluations += sum(student['evaluation'])
                countExams += student['exam']
                countFilteredStudents += 1
            if student['sex'] == value == 'f':
                countEvaluations += sum(student['evaluation'])
                countExams += student['exam']
                countFilteredStudents += 1
        elif whatCount == 'exp':
            if student['experience'] == value == True:
                countEvaluations += sum(student['evaluation'])
                countExams += student['exam']
                countFilteredStudents += 1
            if student['experience'] == value == False:
                countEvaluations += sum(student['evaluation'])
                countExams += student['exam']
                countFilteredStudents += 1

    countEvaluations = round(countEvaluations / (countFilteredStudents * countOfEvaluations), 1)
    countExams = round(countExams / countFilteredStudents, 1)
    return countEvaluations, countExams

def bestStudents():
    bestStudentsList = ''
    averageStudentsRating = []

    for student in students:
        bestCountingFormula = (0.6 * (sum(student['evaluation']) \
                              / countOfEvaluations)) + (0.4 * student['exam'])
        averageStudentsRating.append(bestCountingFormula)
    for index, bestStudent in enumerate(averageStudentsRating):
        if averageStudentsRating[index] == max(averageStudentsRating):
            bestStudentsList += '\n- ' + (students[index]['name'] + ' ' + students[index]['surname'])
      # bestStudentsList сделал строкой, так как в дальнейшем использование этого списка не запланировано
      # и строка выводится красивее. Уверен есть другой способ, но не стал думать :)

    return bestStudentsList

print('\n' * 100)
print('Средние отценки:\n- Домашние задания: {}\
       \n- Экзамен: {}'.format(averageEvaluations()[0], averageEvaluations()[1]) )
print('\nСредняя отценка Мужчин\n- Домашние задания: {}\n- Экзамен: {}' \
       .format(averageRatingsCount('sex', 'm')[0], averageRatingsCount('sex', 'm')[1]) )
print('\nСредняя отценка Женщин\n- Домашние задания: {}\n- Экзамен: {}' \
       .format(averageRatingsCount('sex', 'f')[0], averageRatingsCount('sex', 'f')[1]) )
print('\nСредняя отценка студентов с Опытом\n- : Домашние задания: {}\n- Экзамен: {}' \
       .format(averageRatingsCount('exp', True)[0], averageRatingsCount('exp', True)[1]) )
print('\nСредняя отценка студентов без Опыта\n- : Домашние задания: {}\n- Экзамен: {}' \
       .format(averageRatingsCount('exp', False)[0], averageRatingsCount('exp', False)[1]) )
print('\nЛучший(е) студент(ы): {}' \
      .format(bestStudents()) )
