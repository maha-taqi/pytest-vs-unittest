import unittest
from unittest import mock
import builtins
from quiz import Question, run_quiz, questions

class Test(unittest.TestCase):
    def test_run_quiz_with_no_answers(self):
        # Simulate no answers provided by the user
        input_values = iter(['', '', ''])

        def mock_input(s):
            return next(input_values)

        with mock.patch.object(builtins, 'input', mock_input):
            self.assertRaises(TypeError, run_quiz, questions)


    def test_run_quiz_with_all_correct_answers(self):
        # Simulate no answers provided by the user
        input_values = iter(['c', 'a', 'b'])

        def mock_input(s):
            return next(input_values)

        with mock.patch.object(builtins, 'input', mock_input):
            output = run_quiz(questions)
            self.assertEqual(output, "You got 3 out of 3 correct.")

    def test_run_quiz_with_all_incorrect_answers(self):
        # Simulate all incorrect answers provided by the user
        input_values = iter(['b', 'c', 'a'])

        def mock_input(s):
            return next(input_values)

        with mock.patch.object(builtins, 'input', mock_input):
            output = run_quiz(questions)
            self.assertEqual(output, "You got 0 out of 3 correct.")

if __name__ == "__main__":
    unittest.main()
