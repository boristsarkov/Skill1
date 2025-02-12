import random

# список учеников
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
# отсортируем список учеников
students.sort()
# список предметов
classes = ['Математика', 'Русский язык', 'Информатика']
# пустой словарь с оценками по каждому ученику и предмету
students_marks = {}
# сгенерируем данные по оценкам:
# цикл по ученикам
for student in students:  # 1 итерация: student = 'Александра'
    students_marks[student] = {}  # 1 итерация: students_marks['Александра'] = {}
    # цикл по предметам
    for class_ in classes:  # 1 итерация: class_ = 'Математика'
        marks = [random.randint(1, 5) for i in range(3)]  # генерируем список из 3х случайных оценок
        students_marks[student][class_] = marks  # students_marks['Александра']['Математика'] = [5, 5, 5]
# выводим получившийся словарь с оценками:
for student in students:
    print(f'''{student}
            {students_marks[student]}''')

while True:
    print('''
            Список команд:
            1. Добавить оценки ученика по предмету
            2. Вывести средний балл по всем предметам по каждому ученику
            3. Вывести все оценки по всем ученикам
            4. Вывести информацию по всем оценкам конкретного ученика
            5. Редактирование данных
            6. Вывести средний бал по одному предмету, одного ученика
            7. Выход из программы
            ''')
    command = int(input('Введите команду: '))
    if command == 1:
        print('1. Добавить оценку ученика по предмету')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # считываем название предмета
        class_ = input('Введите предмет: ')
        # считываем оценку
        mark = int(input('Введите оценку: '))
        # если данные введены верно
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            # добавляем новую оценку для ученика по предмету
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        # неверно введены название предмета или имя ученика
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 2:
        print('2. Вывести средний балл по всем предметам по каждому ученику')
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                # находим сумму оценок по предмету
                marks_sum = sum(students_marks[student][class_])
                # находим количество оценок по предмету
                marks_count = len(students_marks[student][class_])
                # выводим средний балл по предмету
                print(f'{class_} - {marks_sum // marks_count}')
            print()
    elif command == 3:
        print('3. Вывести все оценки по всем ученикам')
        print(len(students_marks))
        for key, value in students_marks.items():
            print(f' {key}: ')
            for i, j in value.items():
                print(f'\t {i} {j}')
            print()
    elif command == 4:
        print('4. Вывести информацию по всем оценкам конкретного ученика')
        name = input('Введите имя ученика')
        if name in students_marks:
            ind_name = students.index(name)
            print(f'{students[ind_name]} {students_marks[name]}')
        else:
            print('Студента с таким именем нет!!!')
    elif command == 5:
        print('Редактировать данные')

        while True:
            print('''Список команд для редактирования:
                            1. Удалить оценку 
                            2. Редактировать оценки
                            3. Редактировать ученика
                            4. Удалить ученика
                            5. Редактировать предмет
                            6. Удалить предмет
                            7. Вернуться назад
                            ''')
            command = int(input('Введите команду: '))
            if command == 1:
                student_name = input('Введите имя студента')
                if student_name in students:
                    student_discipline = input('Введите дисциплину')
                    if student_discipline in students_marks.values() or classes:
                        index_student_name = students.index(student_name)
                        index_marks = students_marks[student_name][student_discipline]
                        print(f'{students[index_student_name]}: \n \t {student_discipline}, {index_marks}')
                        index_number = int(input('Введите номер оценки которую хотите удалить (от 1 до 3)'))
                        index_number = index_number - 1
                        del index_marks[index_number]
                        print(f'{students[index_student_name]}: \n \t {student_discipline}, {index_marks}')
                    else:
                        print('Такой дисциплины в списке нет')
                else:
                    print('Студента нет в списках')
            if command == 2:
                student_name = input('Введите имя студента')
                if student_name in students:
                    student_discipline = input('Введите дисциплину')
                    if student_discipline in classes:
                        index_student_name = students.index(student_name)
                        index_marks = students_marks[student_name][student_discipline]
                        print(f'{students[index_student_name]}: \n \t {student_discipline}, {index_marks}')
                        index_number = int(input('Введите номер оценки которую хотите исправить (от 1 до 3)'))
                        new_mark = int(input('Введите новую оценку'))
                        index_number = index_number - 1
                        index_marks[index_number] = new_mark
                        print(f'{students[index_student_name]}: \n \t {student_discipline}, {index_marks}')
                    else:
                        print('Такой дисциплины в списке нет')
                else:
                    print('Студента нет в списках')
            if command == 3:
                student_name = input('Введите имя ученика которого нужно отредактировать')
                if student_name in students_marks:
                    new_name = input('Введите новое имя')
                    students_marks[new_name] = students_marks[student_name]
                    del students_marks[student_name]
                    students_marks = dict(sorted(students_marks.items()))
                else:
                    print('Нет такого имени')
            if command == 4:
                student_name = input('Введите имя студента которого хотите удалить')
                if student_name in students:
                    del students_marks[student_name]
                else:
                    print('Студент не найден')
            if command == 5:
                student_name = input('Введите имя студента')
                if student_name in students:
                    student_discipline = input('Введите дисциплину название которой нужно изменить')
                    if student_discipline in classes:
                        ind_classes = classes.index(student_discipline)
                        index_student_name = students.index(student_name)
                        index_marks = students_marks[student_name][student_discipline]
                        print(f'{students[index_student_name]}: \n \t {student_discipline} - {index_marks}')
                        new_discipline = input('Введите новое название дисциплины')
                        students_marks[student_name][new_discipline] = students_marks[student_name][student_discipline]
                        del students_marks[student_name][student_discipline]
                    else:
                        print('Нет такой дисциплины')
            if command == 6:
                student_name = input('Введите имя студента')
                if student_name in students:
                    student_discipline = input('Введите дисциплину которую нужно удалить')
                    if student_discipline in classes:
                        del students_marks[student_name][student_discipline]
                    else:
                        print('Нет такой дисциплины')
            elif command == 7:
                print('7. Вернуться назад')
                break
    elif command == 6:
        print('6. Вывести средний бал по одному предмету, одного ученика')
        student_name = input('Введите имя студента')
        if student_name in students_marks:
            discipline = input('Введите дисциплину')
            if discipline in classes:
                find_discipline = list(students_marks[student_name].keys())
                ind_discipline = find_discipline.index(discipline)
                mark_sum = sum(students_marks[student_name][discipline])
                mark_count = len(students_marks[student_name][discipline])
                print(f'Средний бал студента {student_name} по дисциплине "{find_discipline[ind_discipline]}" - '
                      f'{mark_sum // mark_count}: ')
            else:
                print('В списке нет такой дисциплины')
        else:
            print('Нет ученика с таким именем')
    elif command == 7:
        print('7. Выход из программы')
        break

