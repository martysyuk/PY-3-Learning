# Домашнее задание по уроку 1-5
# «Практика по использованию циклов, коллекций и функций»
# Выполнил Мартысюк Илья PY-3

students = [
    {'name': 'Василий', 'surname': 'Пупкин', 'sex': 'm',
     'experience': True, "evaluation": (9, 7, 4, 2, 7), 'exam': 9},
    {'name': 'Евгений', 'surname': 'Смернов', 'sex': 'm',
     'experience': True, 'evaluation': (10, 10, 9, 3, 7), 'exam': 10},
    {'name': 'Петр', 'surname': 'Смернов', 'sex': 'm',
     'experience': False, 'evaluation': (4, 2, 6, 1, 9), 'exam': 7},
    {'name': 'Дмитрий', 'surname': 'Давыдов', 'sex': 'm',
     'experience': False, 'evaluation': (4, 4, 4, 4, 4), 'exam': 2},
    {'name': 'Татьяна', 'surname': 'Брамс', 'sex': 'f',
     'experience': True, 'evaluation': (7, 9, 3, 10, 10), 'exam': 10},
    {'name': 'Мария', 'surname': 'Крынкина', 'sex': 'f',
     'experience': False, 'evaluation': (9, 8, 9, 5, 2), 'exam': 5}
]

count_of_students = len(students)
count_of_evaluations = len(students[0]['evaluation'])


def average_evaluations():
    count_of_all_evaluation = 0
    count_of_all_exam = 0

    for student in students:
        count_of_all_evaluation += sum(student['evaluation'])
        count_of_all_exam += student['exam']

        count_of_all_evaluation = round(count_of_all_evaluation / (count_of_students * count_of_evaluations), 1)
        count_of_all_exam = round(count_of_all_exam / count_of_students, 1)
    return count_of_all_evaluation, count_of_all_exam


def average_ratings_count(what_count, value):
    count_evaluations = 0
    count_exams = 0
    count_filtered_students = 0

    for student in students:
        if what_count == 'sex':
            if student['sex'] == value == 'm':
                count_evaluations += sum(student['evaluation'])
                count_exams += student['exam']
                count_filtered_students += 1
            if student['sex'] == value == 'f':
                count_evaluations += sum(student['evaluation'])
                count_exams += student['exam']
                count_filtered_students += 1
        elif what_count == 'exp':
            if student['experience'] == value == True:
                count_evaluations += sum(student['evaluation'])
                count_exams += student['exam']
                count_filtered_students += 1
            if student['experience'] == value == False:
                count_evaluations += sum(student['evaluation'])
                count_exams += student['exam']
                count_filtered_students += 1

    count_evaluations = round(count_evaluations
                              / (count_filtered_students
                                 * count_of_evaluations), 1)
    count_exams = round(count_exams / count_filtered_students, 1)
    return count_evaluations, count_exams


def best_students():
    best_students_list = ''
    average_students_rating = []

    for student in students:
        best_counting_formula = (0.6 * (sum(student['evaluation'])
                                        / count_of_evaluations)) \
                                + (0.4 * student['exam'])
        average_students_rating.append(best_counting_formula)
    for index, bestStudent in enumerate(average_students_rating):
        if average_students_rating[index] == max(average_students_rating):
            best_students_list += '\n- ' + (students[index]['name'] + ' ' + students[index]['surname'])
            # bestStudentsList сделал строкой, так как в дальнейшем использование этого списка не запланировано
            # и строка выводится красивее. Уверен есть другой способ, но не стал думать :)

    return best_students_list


print('\n' * 100)
print('Средние отценки:\n- Домашние задания: {}\n- Экзамен: {}'
      .format(average_evaluations()[0], average_evaluations()[1]))
print('\nСредняя отценка Мужчин\n- Домашние задания: {}\n- Экзамен: {}'
      .format(average_ratings_count('sex', 'm')[0],
              average_ratings_count('sex', 'm')[1]))
print('\nСредняя отценка Женщин\n- Домашние задания: {}\n- Экзамен: {}'
      .format(average_ratings_count('sex', 'f')[0],
              average_ratings_count('sex', 'f')[1]))
print('\nСредняя отценка студентов с Опытом\n- : Домашние задания: {}'
      '\n- Экзамен: {}'.format(average_ratings_count('exp', True)[0],
                               average_ratings_count('exp', True)[1]))
print('\nСредняя отценка студентов без Опыта\n- : Домашние задания: {}'
      '\n- Экзамен: {}'.format(average_ratings_count('exp', False)[0],
                               average_ratings_count('exp', False)[1]))
print('\nЛучший(е) студент(ы): {}'.format(best_students()))
