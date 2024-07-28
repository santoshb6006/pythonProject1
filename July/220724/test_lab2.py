import pytest
import allure

@allure.title("TC1_Smoke test")
@allure.description("We'll be running the smoke test suite")
@pytest.mark.smoke
def test_addition():
    assert 5+9 ==14
@allure.title("TC2_Regression case")
@allure.description("We'll be running the regression suite")
@pytest.mark.regression
def test_sub1():
    assert 15-9 ==6

@allure.title("TC3_Skipping this test case")
@allure.description("We'll be skipping this case")
@pytest.mark.skip(reason="Not working properly, so skip it")
def test_sub2():
    assert 30-9 ==21
@allure.title("TC4_Smoke test")
@allure.description("We'll be running the sanity suite")
@pytest.mark.smoke
def test_mul():
    assert 15*6 ==90
