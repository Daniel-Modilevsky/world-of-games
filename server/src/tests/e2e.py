# This file will have two functions.
# Functions
# 1. test_scores_service - it’s purpose is to test our web service. It will get the application
# URL as an input, open a browser to that URL, select the score element in our web page,
# check that it is a number between 1 to 1000 and return a boolean value if it’s true or not.
from selenium import webdriver


def test_scores_service(url):
    driver = webdriver.Chrome() # initialize a Chrome browser
    driver.get(url) # navigate to the given URL

    # find the score element and extract its text
    score_element = driver.find_element_by_id("score")
    score_text = score_element.text

    # check if the score is a number between 1 and 1000
    try:
        score = int(score_text)
        return 1 <= score <= 1000
    except ValueError:
        return False
    finally:
        driver.quit() # close the browser window


# 2. main_function to call our tests function. The main function will return -1 as an OS exit
# code if the tests failed and 0 if they passed.
def run_scores_file_test():
    exit_code = test_scores_service("http://127.0.0.1:30000")
    exit_status = -1 if not exit_code else 0
    exit(exit_status)


run_scores_file_test()


# TODO: The scores file have acess from aoutside to run it locally and affect on it.
