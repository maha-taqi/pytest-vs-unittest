import pytest
import mock
from quiz import run_quiz, questions
import builtins


def test_run_quiz_with_no_answers():
    # Mock user input to simulate no answers provided
    input_values = iter(['', '', ''])
    def mock_input(s):
        return next(input_values)

    with pytest.raises(TypeError):
        with mock.patch.object(builtins, 'input', mock_input):
            assert run_quiz(questions) == "You got 0 out of 3 correct."


def test_run_quiz_with_correct_answers():
    # Mock user input to simulate the correct answer provided
    input_values = iter(['c', 'a', 'b'])
    def mock_input(s):
        return next(input_values)

    with mock.patch.object(builtins, 'input', mock_input):
        assert run_quiz(questions) == "You got 3 out of 3 correct."


def test_run_quiz_with_incorrect_answers():
    # Mock user input to simulate wrong answers provided
    input_values = iter(['b', 'c', 'a'])
    def mock_input(s):
        return next(input_values)

    with mock.patch.object(builtins, 'input', mock_input):
        assert run_quiz(questions) == "You got 0 out of 3 correct."


def test_run_quiz_with_incorrect_input():
    # Mock user input to simulate the wrong type
    input_values = iter(['y', 'x', 'z'])

    def mock_input(s):
        return next(input_values)

    with pytest.raises(TypeError):
        with mock.patch.object(builtins, 'input', mock_input):
            run_quiz(questions)

if __name__ == "__main__":
    pytest.main()
