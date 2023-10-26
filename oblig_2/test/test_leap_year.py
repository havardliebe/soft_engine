import pytest
from leap_year import isLeapYear

# Tester for skuddår
def test_leap_year_dividible_by_4_but_not_100():
    assert isLeapYear(2004) == True
    assert isLeapYear(2016) == True
    assert isLeapYear(2020) == True

def test_leap_year_dividible_by_400():
    assert isLeapYear(2000) == True
    assert isLeapYear(2400) == True

# Tester for ikke-skuddår
def test_non_leap_year_not_dividible_by_4():
    assert isLeapYear(2017) == False
    assert isLeapYear(2021) == False

def test_non_leap_year_dividible_by_100_but_not_400():
    assert isLeapYear(1700) == False
    assert isLeapYear(1800) == False
    assert isLeapYear(1900) == False
    assert isLeapYear(2100) == False
