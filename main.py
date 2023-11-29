courses = ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python", "Frontend-разработчик с нуля"]

mentors = [
	["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
	["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
	["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
	["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]

durations = [14, 20, 12, 20]

courses1 = ["Python-разработчик с нуля", "Java-разработчик с нуля"]

courses2 = ["Fullstack-разработчик на Python", "Frontend-разработчик с нуля"]

mentors1 = [
	["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
	["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"]
]

mentors2 = [
	["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
	["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]


# функция для определения топ-3 популярных имён среди преподавателей
def top3_mentors(mentors):
    all_list = []
    for m in mentors:
        all_list.extend(m)
    all_names_list = []
    for mentor in all_list:
        name = (mentor.split())[0]
        all_names_list.append(name)
    unique_names = list(set(all_names_list))
    popular = []
    for name in unique_names:
        popular.append([name, all_names_list.count(name)])
    popular.sort(key=lambda x:x[1], reverse=True)
    top_3 = list(popular[:3])
    top = [f"{str(i[0])}: {str(i[1])} раз(а)" for i in top_3]
    return f'{top[0]}, {top[1]}, {top[2]}'

# print(top3_mentors(mentors))


# функция для нахождения самого продолжительного и самого короткого курса по программированию
def min_max_courses(courses, mentors, durations):
    courses_list = []
    for course, mentor, duration in zip(courses, mentors, durations):
        course_dict = {
        "title": course,
        "mentors": mentor,
        "duration": duration
      }
        courses_list.append(course_dict)
    min_ = min(durations)
    max_ = max(durations)
    maxes = []
    minis = []
    for index, duration in enumerate(durations):
        if duration == max_:
            maxes.append(index)
        elif duration == min_:
            minis.append(index)
    courses_min = []
    courses_max = []
    for id in minis:
        courses_min.append(courses_list[id]["title"])
    for id in maxes:
        courses_max.append(courses_list[id]["title"])
    return (f'Самый короткий курс(ы): {", ".join(courses_min)} - {min_} месяца(ев). '
            f'Самый длинный курс(ы): {", ".join(courses_max)} - {max_} месяца(ев)')


# print(min_max_courses(courses, mentors, durations).split('.')[1])

#функция для подсчета тёзок на каждом курсе
def same_names_courses(courses, mentors):
    global same_name_list_sort
    courses_list = []
    for course, mentor in zip(courses, mentors):
        course_dict = {"title":course, "mentors":mentor}
        courses_list.append(course_dict)
    total_list = []
    for course in courses_list:
        all_name_list = [i.split(' ')[0] for i in course ['mentors']]
        unique_names = set(all_name_list)
        same_name_list = []
        for set_name in unique_names:
            if all_name_list.count(set_name) > 1:
                for fio in course['mentors']:
                    if set_name in fio:
                        same_name_list.append(fio)
                        same_name_list_sort = sorted(same_name_list)
        if same_name_list_sort:
            total_list.append(f'На курсе {course["title"]} есть тёзки: {", ".join(same_name_list_sort)}')
    return total_list


# print(same_names_courses(courses, mentors))

