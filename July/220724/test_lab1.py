import pytest
import allure
@pytest.mark.smoke
def test_addition():
    # assert-? assertion-what you want to validate?
    assert 1 + 1 == 2

@pytest.mark.sanity
def test_sub():
    assert 5 - 2 == 3

@pytest.mark.regression
def test_mul():
    assert 5 * 2 == 10

@pytest.mark.skip(reason="Not working, so we are skipping")
def test_div():
    assert 15 / 5 == 3
