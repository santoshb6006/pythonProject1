import allure
import pytest
import requests


@allure.title("Test GET Request-RestFUL Booker Project#1")
@allure.description("TC#1-> Verify that GET Request with ID Works")
@allure.tag("regression", "p0", "smoke")
@allure.testcase("TC#1")
@pytest.mark.smoke

def test_get_single_request_by_id():
    url="https://restful-booker.herokuapp.com/booking/:1"
    responseData= requests.get(url)
    print(responseData.json())
    assert responseData.status_code ==200