import string
#https://stackoverflow.com/questions/13166395/fill-input-of-type-text-and-press-submit-using-python
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

username = "jonas.dahl"

passwordguess = ""

passwordlenght = 17

allcharacters = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"

webpage = "https://portal.regjeringen.uiaikt.no/"  # Edit the URL
searchterm = "YourUsername"  # Edit the username

# Ensure you have the correct path to your ChromeDriver executable
chrome_driver_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'

# Set up the Chrome WebDriver
driver = webdriver.Chrome()
driver.get(webpage)

driver.find_element(By.NAME, "username").send_keys(username)

passwordguess = "qwertyuioplkjhgfd"

driver.find_element(By.NAME, "password").send_keys(passwordguess)

driver.find_element(By.CLASS_NAME, "btn-primary").click()

# Wait for user input before closing the browser
input("Press Enter to close the browser...")

# Close the browser window
driver.quit()

# Locate the search box and submit button by class name
#sbox = driver.find_element_by_class_name("formcontroll")
#submit = driver.find_element_by_class_name("btn btn-primary btn-block")

# Input the search term and submit the form
#sbox.send_keys(searchterm)
#submit.click()


print(username)






