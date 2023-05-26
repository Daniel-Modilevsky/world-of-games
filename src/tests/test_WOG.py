from src.games.CurrencyRouletteGame import calculate_money_interval
from src.games.GuessGame import compare_results
from src.games.MemoryGame import is_list_equal
from src.utils.games_utils import is_in_range


# Tests for the is_in_range function
def test_is_in_range_with_number_in_range():
    assert is_in_range(1, 10, 5) == False
    assert is_in_range(4, 1, 10) == True


def test_calculate_money_interval():
    assert calculate_money_interval(1, 10) == [4, 6]
    assert calculate_money_interval(5, 60) == [50, 60]


def test_compare_results():
    assert compare_results([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
    assert not compare_results([1, 2, 3, 4], [1, 2, 3, 4, 5])
    assert compare_results([], [])


def test_is_list_equal():
    assert is_list_equal([1, 2, 3, 4], [1, 2, 3, 4])
    assert not is_list_equal([2, 2, 2, 2], [1, 1, 1, 1])

