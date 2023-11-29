import pytest
from main import (courses, mentors, durations, courses1, courses2, mentors1, mentors2, top3_mentors,
                  min_max_courses, same_names_courses)


#тесты для функции top3_mentors
class TestTop3Mentors():
    mentors = mentors
    # проверяем, что топ действительно состоит из 3х имен
    def test_1_top3(self):
        expected = 3
        result = len(top3_mentors(self.mentors).split(','))
        assert result == expected

    #проверяем, что на первом месте в топе самое большое число
    def test_2_top3(self):
        top1 = int(top3_mentors(self.mentors).split()[1])
        top2 = int(top3_mentors(self.mentors).split()[4])
        top3 = int(top3_mentors(self.mentors).split()[7])
        assert (top1 > top2 and top1 > top3)


#тесты для функции min_max_courses
class TestMinMaxCourses():
    courses = courses
    mentors = mentors
    durations = durations

    # проверяем, что длительность самого короткого курса 12 месяцев
    def test_1_min_max_courses(self):
        expected = 12
        result = int(min_max_courses(self.courses, self.mentors, self.durations).split()[7])
        assert result == expected

    #проверяем, среди самых длительных курсов есть "Frontend-разработчик с нуля"
    def test_2_min_max_courses(self):
        expected = "Frontend-разработчик с нуля"
        result = min_max_courses(self.courses, self.mentors, self.durations).split('.')[1]
        assert expected in result


#тест для функции same_names_courses
@pytest.mark.parametrize(
    "courses_,mentors_,expected",
    [
        (courses1, mentors1, 'Александр Бардин'),
        (courses2, mentors2, 'Евгений Шек'),
    ]
)
def test_same_names_courses(courses_, mentors_, expected):
    result = same_names_courses(courses_, mentors_)[0]
    assert expected in result

