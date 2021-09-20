import pytest
import tasks as task


class TestTask1:
    """Tests for Task 1"""

    @pytest.mark.parametrize('n,exp,expected', [(2, 3, 8), (2, 1, 2), (2, 0, 1)])
    def test_int_input(self, n, exp, expected):
        assert task.to_power(n, exp) == expected
    
    def test_negative_input(self):
        with pytest.raises(ValueError) as e:
            task.to_power(2, -1)
    

class TestTask2:
    """Tests for Task 2"""
    @pytest.mark.parametrize('word,expected', [
                                               ('abba', True), 
                                               ('mom', True), 
                                               ('AnNa', True),
                                               ('123321', True),
                                               ('', True),
                                               ('I', True),
                                               ('pijama', False),
                                              ])
    def test_palindrome(self, word, expected):
        assert task.is_palindrome(word) == expected

    def test_int_input(self):
        with pytest.raises(ValueError) as e:
            task.is_palindrome(0)


class TestTask3:
    """Tests for Task 2"""
    
    @pytest.mark.parametrize('n,exp,expected', [(2, 4, 8), (2, 0, 0), (9, 9, 81)])
    def test_int_input(self, n, exp, expected):
        assert task.mult(n, exp) == expected
    
    def test_negative_input(self):
        with pytest.raises(ValueError):
            task.mult(2, -1)

    def test_float(self):
        with pytest.raises(TypeError):
            task.mult(2.0, 1)


class TestTask4:
    """Tests for Task 2"""

    @pytest.mark.parametrize('input_str,expected', [('hello', 'olleh'), ('o', 'o'), ('', '')])
    def test_reverse(self, input_str, expected):
        assert task.reverse(input_str) == expected


class TestTask5:
    """Tests for Task 2"""
    @pytest.mark.parametrize('n,expected', [('123', 6), ('999', 27), ('0', 0)])
    def test_digit_input(self, n, expected):
        assert task.sum_of_digits(n) == expected
    
    def test_nondigit_input(self):
        with pytest.raises(ValueError):
            task.sum_of_digits('12a3')


