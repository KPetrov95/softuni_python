from unittest import TestCase, main
from project.student import Student



class StudentTests(TestCase):
    def setUp(self):
        self.test_student_one = Student("Gosho")
        self.test_student_two = Student("Pesho", {'PB': ['n1', 'n2', 'n3']})

    def test_init_no_courses(self):
        self.assertEqual(self.test_student_one.name, "Gosho")
        self.assertEqual({}, self.test_student_one.courses)

    def test_init_with_courses(self):
        self.assertEqual('Pesho', self.test_student_two.name)
        self.assertEqual({'PB': ['n1', 'n2', 'n3']}, self.test_student_two.courses)

    def test_enroll_course_already_added(self):
        result = self.test_student_two.enroll(course_name='PB', notes=['n4', 'n5'], add_course_notes='N')
        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual({'PB': ['n1', 'n2', 'n3', 'n4', 'n5']}, self.test_student_two.courses)

    def test_enroll_course_new_course(self):
        result = self.test_student_two.enroll(course_name='JS', notes=['n4', 'n5'], add_course_notes='')
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual({'PB': ['n1', 'n2', 'n3'], 'JS': ['n4', 'n5']}, self.test_student_two.courses)

    def test_enroll_course_new_course_with_y(self):
        result = self.test_student_two.enroll(course_name='JS', notes=['n4', 'n5'], add_course_notes='Y')
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual({'PB': ['n1', 'n2', 'n3'], 'JS': ['n4', 'n5']}, self.test_student_two.courses)


    def test_enroll_course_no_notes(self):
        result = self.test_student_two.enroll(course_name='JS', notes=['n4', 'n5'], add_course_notes='N')
        self.assertEqual("Course has been added.", result)
        self.assertEqual({'PB': ['n1', 'n2', 'n3'], 'JS': []}, self.test_student_two.courses)

    def test_add_notes_success(self):
        result = self.test_student_two.add_notes(course_name='PB', notes='N1')
        self.assertEqual("Notes have been updated", result)
        self.assertEqual({'PB': ['n1', 'n2', 'n3', 'N1']}, self.test_student_two.courses)

    def test_add_notes_course_not_found(self):
        with self.assertRaises(Exception) as ex:
            self.test_student_one.add_notes(course_name='PB', notes=['N1'])
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course_success(self):
        result = self.test_student_two.leave_course('PB')
        self.assertEqual({}, self.test_student_two.courses)
        self.assertEqual("Course has been removed", result)

    def test_leave_course_course_not_found(self):
        with self.assertRaises(Exception) as ex:
            self.test_student_one.leave_course('PB')
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

if __name__ == "__main__":
    main()