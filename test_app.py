#from app import add_numbers
from app import check_guess

def test_check_guess_low():
    assert check_guess(3, 7) == "low"

def test_check_guess_high():
    assert check_guess(9, 7) == "high"

def test_check_guess_correct():
    assert check_guess(7, 7) == "correct"



#def test_addition_correct():
#    assert add_numbers(2, 3) == 5

# Optional: a deliberately failing test to demo CI catching failures
# def test_addition_fail():
#     assert add_numbers(2, 3) == 6