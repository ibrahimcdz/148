# TODO: Add the test cases that you'll be submitting to this file!
#       Make sure your test cases are all named starting with
#       test_ and that they have unique names.
import pytest
from course import Student, Course
from survey import CheckboxQuestion, MultipleChoiceQuestion, Answer, \
    InvalidAnswerError, NumericQuestion, YesNoQuestion, Survey
from criterion import HomogeneousCriterion
from grouper import Group, AlphaGrouper, Grouping, GreedyGrouper
from example_tests import compare_groupings
# You may need to import pytest in order to run your tests.
# You are free to import hypothesis and use hypothesis for testing.
# This file will not be graded for style with PythonTA

###############################################################################
# Task 2 Test cases
###############################################################################
class TestStudent:
    def test_has_answer(self) -> None:
        luffy = Student(1, 'Luffy')
        options = ['a. the red line', 'b. lodestar island', 'c. water 7']
        all_blue = MultipleChoiceQuestion(1, 'where is the all blue?', options)
        luffy_answer = Answer('c. water 7')
        luffy.set_answer(all_blue, luffy_answer)
        assert luffy.has_answer(all_blue) is True

    def test_set_answer_override(self) -> None:
        luffy = Student(1, 'Luffy')
        zoro = Student(2, 'Zoro')
        options = ['a. the red line', 'b. lodestar island', 'c. water 7']
        all_blue = MultipleChoiceQuestion(1, 'where is the all blue?', options)
        luffy_answer = Answer('c. water 7')
        zoro_answer = Answer('b. lodestar island')
        assert luffy.set_answer(all_blue, luffy_answer) is None
        assert zoro.set_answer(all_blue, zoro_answer) is None
        assert luffy.has_answer(all_blue) is True
        assert zoro.has_answer(all_blue) is True

    def test_get_answer(self) -> None:
        luffy = Student(1, 'Luffy')
        zoro = Student(2, 'Zoro')
        options = ['a. the red line', 'b. lodestar island', 'c. water 7']
        all_blue = MultipleChoiceQuestion(1, 'where is the all blue?', options)
        luffy_answer = Answer('c. water 7')
        zoro_answer = Answer('b. lodestar island')
        luffy.set_answer(all_blue, luffy_answer)
        zoro.set_answer(all_blue, zoro_answer)
        assert zoro.get_answer(all_blue) == zoro_answer
        assert luffy.get_answer(all_blue) == luffy_answer

    def test_none_cases(self) -> None:
        luffy = Student(1, 'Luffy')
        zoro = Student(2, 'Zoro')
        options = ['a. the red line', 'b. lodestar island', 'c. water 7']
        all_blue = MultipleChoiceQuestion(1, 'where is the all blue?', options)
        luffy_answer = Answer('c. water 7')
        luffy.set_answer(all_blue, luffy_answer)
        assert zoro.get_answer(all_blue) is None
        assert luffy.get_answer(all_blue) is luffy_answer
        luffy_new_answer = Answer('a. the red line')
        luffy.set_answer(all_blue, luffy_new_answer)
        assert luffy.get_answer(all_blue) is luffy_new_answer

    def test_non_valid_option(self) -> None:
        luffy = Student(1, 'Luffy')
        zoro = Student(2, 'Zoro')
        options = ['a. the red line', 'b. lodestar island', 'c. water 7']
        all_blue = MultipleChoiceQuestion(1, 'where is the all blue?', options)
        luffy_answer = Answer('c. water 7')
        luffy.set_answer(all_blue, luffy_answer)
        zoro_answer = Answer('q. hahaha')
        zoro.set_answer(all_blue, zoro_answer)
        assert zoro.has_answer(all_blue) is False

###############################################################################
# Task 3 Test cases
###############################################################################
class TestCourse:
    def test_enroll_students(self) -> None:
        luffy = Student(1, 'Luffy')
        zoro = Student(2, 'Zoro')
        new_list = [luffy, zoro]
        course = Course('Math')
        course.enroll_students(new_list)
        assert course.students == [luffy, zoro]

    def test_enroll_students_id_duplicate(self) -> None:
        luffy = Student(1, 'Luffy')
        zoro = Student(1, 'Zoro')
        new_list = [luffy, zoro]
        course = Course('Math')
        course.enroll_students(new_list)
        assert course.students == []

    def test_all_answered(self) -> None:
        luffy = Student(1, 'Luffy')
        zoro = Student(2, 'Zoro')
        abc = YesNoQuestion(1, 'what is it?')
        cba = MultipleChoiceQuestion(1, 'which one?', ['a', 'b', 'c'])
        luffy_answer = Answer('a')
        luffy.set_answer(cba, luffy_answer)
        zoro_answer = Answer('b')
        zoro.set_answer(cba, zoro_answer)
        new_list = [luffy, zoro]
        course = Course('Math')
        course.enroll_students(new_list)
        new_survey = Survey([abc])
        assert course.all_answered(new_survey) is False
        renew_survey = Survey([cba])
        assert course.all_answered(renew_survey) is True

    def test_get_students(self) -> None:
        luffy = Student(2, 'Luffy')
        zoro = Student(1, 'Zoro')
        new_list = [luffy, zoro]
        course = Course('Math')
        course.enroll_students(new_list)
        assert course.get_students() == (zoro, luffy)

###############################################################################
# Task 4 Test cases
###############################################################################


###############################################################################
# Task 5 Test cases
###############################################################################
# TODO: Add your test cases below


###############################################################################
# Task 6 Test cases
###############################################################################

def test_score_answers()-> None:
    a = YesNoQuestion(1, 'blah')
    b = Answer(True)
    d = Answer(True)
    answers = [b,d]
    bah = HomogeneousCriterion()
    score = bah.score_answers(a, answers)
    assert score == 1.0
###############################################################################
# Task 7 Test cases
###############################################################################
class TestGroup:
    def test_group___contains__(self) -> None:
        luffy = Student(1, 'Luffy')
        zoro = Student(2, 'Zoro')
        chopper = Student(3, 'Chopper')
        students = [luffy, zoro, chopper]
        group = Group(students)
        assert group.__contains__(luffy) is True

    def test_group___len__(self) -> None:
        luffy = Student(1, 'Luffy')
        zoro = Student(2, 'Zoro')
        chopper = Student(3, 'Chopper')
        students = [luffy, zoro, chopper]
        group = Group(students)
        assert group.__len__() is 3

    def test_group_get_members(self) -> None:
        luffy = Student(1, 'Luffy')
        zoro = Student(2, 'Zoro')
        chopper = Student(3, 'Chopper')
        students = [luffy, zoro, chopper]
        group = Group(students)
        assert group.get_members() == students

###############################################################################
# Task 8 Test cases
###############################################################################
class TestGrouping:
    def test_grouping_add_group(self) -> None:
        grouping = Grouping()
        luffy = Student(1, 'Luffy')
        zoro = Student(2, 'Zoro')
        chopper = Student(3, 'Chopper')
        students = [luffy, zoro, chopper]
        group = Group(students)
        grouping.add_group(group)
        assert group in grouping.get_groups()

###############################################################################
# Task 9 Test cases
###############################################################################
class TestSurvey:
    def test_score_grouping(self) -> None:

        q1 = MultipleChoiceQuestion(1, 'a', ['a', 'b', 'c'])
        q2 = YesNoQuestion(2, 'a')
        q3 = CheckboxQuestion(3, 'a', ['a', 'd', 'e'])
        s1 = Student(1, 'luffy')
        s2 = Student(2, 'zoro')
        s3 = Student(3, 'chopper')
        s1.set_answer(q1, Answer('a'))
        s1.set_answer(q2, Answer(True))
        s1.set_answer(q3, Answer('a'))
        s2.set_answer(q1, Answer('a'))
        s2.set_answer(q2, Answer(True))
        s2.set_answer(q3, Answer('a'))
        s3.set_answer(q1, Answer('a'))
        s3.set_answer(q2, Answer(False))
        s3.set_answer(q3, Answer('d'))
        s = Survey([q1, q2, q3])

        grouping = Grouping()
        grouping.add_group(Group([s1, s2, s3]))
        assert 0.5555555555555555


###############################################################################
# Task 10 Test cases
###############################################################################
class TestAlphaGrouper:
    def test_AlphaGrouper_make_grouping(self) -> None:
        s = Survey([])
        alpha_grouping = AlphaGrouper(3)
        expected_grouping = Grouping()

        luffy = Student(1, 'Luffy')
        zoro = Student(2, 'Zoro')
        chopper = Student(3, 'Chopper')
        nami = Student(4, 'Nami')
        csc148 = Course('CSC148')
        csc148.enroll_students([luffy, zoro, chopper, nami])

        expected_grouping.add_group(Group([chopper, luffy, nami]))
        expected_grouping.add_group(Group([zoro]))

        alpha_grouping.make_grouping(csc148, s)
        assert compare_groupings(expected_grouping, alpha_grouping.make_grouping(csc148, s)) is None


class TestGreedyGrouper:
    def test_greedygrouper_make_grouping(self) -> None:
        q1 = MultipleChoiceQuestion(1, 'a', ['a', 'b', 'c'])
        s = Survey([q1])
        greed_group = GreedyGrouper(2)
        expected_grouping = Grouping()

        answer = Answer('a')
        answer2 = Answer('c')

        luffy = Student(1, 'Luffy')
        luffy.set_answer(q1, answer)
        zoro = Student(2, 'Zoro')
        zoro.set_answer(q1, answer2)
        chopper = Student(3, 'Chopper')
        chopper.set_answer(q1, answer)
        nami = Student(4, 'Nami')
        nami.set_answer(q1, answer2)

        csc148 = Course('CSC148')
        csc148.enroll_students([luffy, zoro, chopper, nami])

        criteria = HomogeneousCriterion()
        criteria.score_answers(q1, [answer, answer2])

        expected_grouping.add_group(Group([luffy, chopper]))
        expected_grouping.add_group(Group([zoro, nami]))

        assert compare_groupings(expected_grouping, greed_group.make_grouping(csc148, s)) is None



