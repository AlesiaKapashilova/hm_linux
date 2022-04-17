import unittest
from school import *


class TestSchool(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.school = School()
        anastasiya = Students("Skachek", 1, [9, 10, 9, 10, 9])
        mirsad = Students("Proshych", 2, [8, 9, 8, 9, 7])
        yauheni = Students('Vinahradau', 2, [5, 5, 6, 6, 5])
        aliaksei = Students("Zhendi", 3, [8, 7, 7, 8, 7])
        cls.school.add_student(anastasiya)
        cls.school.add_student(mirsad)
        cls.school.add_student(yauheni)
        cls.school.add_student(aliaksei)

    @classmethod
    def tearDownCLass(cls):
        print('This is a unittest for School')

    def test_add_student(self):
        answer = len(self.school.students)
        self.assertEqual(answer, 4)

    def test_marks_one_student(self):
        answer = self.school.marks(8, 7)
        self.assertEqual(answer, 'Zhendi ')

    def test_group_one_student(self):
        answer = self.school.group(1)
        self.assertEqual(answer, 'Skachek ')

    def test_automat_one_student(self):
        answer = self.school.automat(9)
        self.assertEqual(answer, 'Skachek ')

    def test_marks_some_students(self):
        answer = self.school.marks(5, 6)
        self.assertEqual(answer, 'Vinahradau ')

    def test_group_some_students(self):
        answer = self.school.group(2)
        self.assertEqual(answer, 'Proshych Vinahradau ')

    def test_automat_some_students(self):
        answer = self.school.automat(5)
        self.assertEqual(answer, 'Skachek Proshych Vinahradau Zhendi ')

    def test_add_student_notequal(self):
        answer = len(self.school.students)
        self.assertNotEqual(answer, 2)

    def test_marks_one_student_notequal(self):
        answer = self.school.marks(6, 7)
        self.assertNotEqual(answer, 'Proshych ')

    def test_group_one_student_notequal(self):
        answer = self.school.group(3)
        self.assertNotEqual(answer, 'Skachek ')

    def test_automat_one_student_notequal(self):
        answer = self.school.automat(7)
        self.assertNotEqual(answer, 'Zhendi ')

    def test_marks_some_students_notequal(self):
        answer = self.school.marks(6, 7)
        self.assertNotEqual(answer, 'Skachek Vinahradau ')

    def test_group_some_students_notequal(self):
        answer = self.school.group(2)
        self.assertNotEqual(answer, 'Skachek Zhendi ')

    def test_automat_some_students_notequal(self):
        answer = self.school.automat(6)
        self.assertNotEqual(answer, 'Skachek Vinahradau ')

    def test_marks_args(self):
        with self.assertRaises(AssertionError) as er:
            self.school.marks(6)
        self.assertEqual('please enter more than 1 mark', er.exception.args[0])

    def test_group_int(self):
        with self.assertRaises(AssertionError) as er:
            self.school.group('1')
        self.assertEqual('group must be int', er.exception.args[0])

    def test_automat_int(self):
        with self.assertRaises(AssertionError) as er:
            self.school.automat('5')
        self.assertEqual('automat must be int', er.exception.args[0])


if __name__ == "__main__":
    unittest.main()
