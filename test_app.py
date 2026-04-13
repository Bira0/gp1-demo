from app import add_numbers

def test_addition_correct():
    assert add_numbers(2, 3) == 5

# Optional: a deliberately failing test to demo CI catching failures
# def test_addition_fail():
#     assert add_numbers(2, 3) == 6