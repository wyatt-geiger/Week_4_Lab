"""
Practice using

 assertTrue
 assertFalse
 assertIsNone
 assertIsNotNone
 assertIn
 assertNotIn

"""

from studentlists import ClassList, StudentError
from unittest import TestCase

class TestStudentLists(TestCase):

    def test_cant_create_class_with_negative_students(self): # test to ensure that the program does not allow negative numbers
        with self.assertRaises(StudentError):
            test_class = ClassList(-1)

    def test_cant_create_class_with_zero_students(self): # test to ensure that the program does not allow 0 students
        with self.assertRaises(StudentError):
            test_class = ClassList(0)

    def test_add_student_check_student_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        self.assertIn('Test Student', test_class.class_list)

        test_class.add_student('Another Test Student')
        self.assertIn('Test Student', test_class.class_list)
        self.assertIn('Another Test Student', test_class.class_list)


    def test_add_student_already_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        with self.assertRaises(StudentError):
            test_class.add_student('Test Student')


    ## FINISHED: write a test that adds and removes a student, 
    # and asserts the student is removed. Use assertNotIn
    def test_add_remove_student_ensure_removed(self):
        # this test checks to make sure that the program does not contain a specific student
        test_class = ClassList(2)
        test_class.add_student('Test Student') # adds a student
        test_class.remove_student('Test Student') # removes a student
        self.assertNotIn('Test Student', test_class.class_list)
        # since this student is not in the class list, this test will pass


    ## FINISHED: write a test that adds some example students, 
    # then removes a student not in the list, and asserts a StudentError is raised
    def test_removing_student_from_populated_list_raises_student_error(self):
        test_class = ClassList(4)
        test_class.add_student('Example') # adds an example student
        test_class.add_student('Another Example') # attempts to remove a student that is not in the list
        with self.assertRaises(StudentError): # if the student is not in the list, this error will be raised
            test_class.remove_student('That student is not in the list')

    ## FINISHED write a test that removes a student from an 
    # empty list, and asserts a StudentError is raised

    def test_remove_student_from_empty_list(self): # this test is used to determine if the program handles dealing with empty lists correctly
        test_class = ClassList(2)
        with self.assertRaises(StudentError): # since the student is not in the list, this error will be raised, and the test will pass
            test_class.remove_student('That student is not in the list')


    def test_is_enrolled_when_student_present(self):
        test_class = ClassList(2)
        test_class.add_student('Snoop Dogg')
        test_class.add_student('Martha Stewart')
        self.assertTrue(test_class.is_enrolled('Snoop Dogg'))
        self.assertTrue(test_class.is_enrolled('Martha Stewart'))


    def test_is_enrolled_empty_class_list(self):
        test_class = ClassList(2)
        self.assertFalse(test_class.is_enrolled('Snoop Dogg'))


    ## FINISHED: write a test that adds some example students to a test class,
    ## then, call is_enrolled for a student who is not enrolled. 
    # Use assertFalse to verify is_enrolled returns False.

    def test_is_enrolled_false(self): # this method tests is_enrolled
        test_class = ClassList(2)
        test_class.add_student('Snoop Dogg')
        test_class.add_student('Martha Stewart')
        # add some example students
        self.assertFalse(test_class.is_enrolled('Bruce Wayne'))
        self.assertFalse(test_class.is_enrolled('Clark Kent'))
        # checks is_enrolled to see if these two students, Bruce and Clark, are in the list. It should return False, meaning the test passed


    def test_string_with_students_enrolled(self):
        test_class = ClassList(2)
        test_class.add_student('Taylor Swift')
        test_class.add_student('Kanye West')
        self.assertEqual('Taylor Swift, Kanye West', str(test_class))


    def test_string_empty_class(self):
        test_class = ClassList(2)
        self.assertEqual('', str(test_class))


    def test_index_of_student_student_present(self):
        test_class = ClassList(3)
        test_class.add_student('Harry')
        test_class.add_student('Hermione')
        test_class.add_student('Ron')

        self.assertEqual(1, test_class.index_of_student('Harry'))
        self.assertEqual(2, test_class.index_of_student('Hermione'))
        self.assertEqual(3, test_class.index_of_student('Ron'))

        # This assert passes, but it's redundant - the first assert statement will fail if
        # the method call returns None
        self.assertIsNotNone(test_class.index_of_student('Harry'))


  
    ## FINISHED write a test for index_of_student when the class_list list is empty.  
    # Assert index_of_student returns None for a student if the list is empty. 
    # use assertIsNone.
 
    def test_index_of_student_when_empty(self): # this test is used to see if the index_of_student method can handle an empty class list 
        test_class = ClassList(3)
        self.assertIsNone(test_class.index_of_student('Test Student'))
        # since the list is empty and therefore returns None, this test will pass

    ## FINISHED write another test for index_of_student. In the case when the 
    # class_list is not empty but has some students.
    # assert that searching for a student name that is not in the list, returns None.

    def test_index_of_student_when_not_empty_not_in_list(self):
        # this test adds students to the list and checks if the program returns None if a student that is tested is not in the list
        test_class = ClassList(3)
        test_class.add_student('Harry')
        test_class.add_student('Hermione')
        test_class.add_student('Ron')
        # this assert checks to make sure that the program returns None since the student (Malfoy) is not in the list
        self.assertIsNone(test_class.index_of_student('Malfoy'))

   
    ## FINISHED: write a test for your new is_class_full method when the class is full. 
    # use assertTrue.

    def test_is_class_full_true(self): # this test checks to see if the program handles a full class list correctly
        test_class = ClassList(3) # size of the class is 3
        test_class.add_student('Harry')
        test_class.add_student('Hermione')
        test_class.add_student('Ron')
        # add 3 example students

        self.assertTrue(test_class.is_class_full(3))
        # this line determines if the class is full. this should return True, therefore the test passes
    
    ## FINISHED: write a test for your new is_class_full method for when is empty, 
    # and when it is not full. Use assertFalse.

    def test_is_class_full_not_full(self): 
        # this test ensures that the program can handle class lists that are not full
        test_class = ClassList(3) # set class size to 3
        test_class.add_student('Ron')
        # add only 1 example student

        self.assertFalse(test_class.is_class_full(3))
        # since there is only 1 example student, this should return False since the list is not full, therefore test should pass

    def test_is_class_full_empty(self):
        # this test ensures that the program can handle class lists that are empty
        test_class = ClassList(3) # set class size to 3

        self.assertFalse(test_class.is_class_full(3))
        # since there are no students in the class list this should return False, meaning the test should pass