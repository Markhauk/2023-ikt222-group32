#https://stackoverflow.com/questions/13166395/fill-input-of-type-text-and-press-submit-using-python
from selenium import webdriver
from selenium.webdriver.common.by import By

username = "jonas.dahl"

passwordguess = ""

passwordlenght = 17

allcharacters = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"

webpage = "https://portal.regjeringen.uiaikt.no/"  # Edit the URL

# Ensure you have the correct path to your ChromeDriver executable
chrome_driver_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'

# Set up the Chrome WebDriver
driver = webdriver.Chrome()
driver.get(webpage)

driver.find_element(By.NAME, "username").send_keys(username)

passwordguess = "qwertyuioplkjhgfd"

driver.find_element(By.NAME, "password").send_keys(passwordguess)

driver.find_element(By.CLASS_NAME, "btn-primary").click()

# Replace 'your_element_locator' with the appropriate locator for your element
# For example, if you want to collect text from a <p> element, you might use By.TAG_NAME and 'p'
# Use By.ID to find the element by its id attribute
response_message_element = driver.find_element(By.ID, "responseMessage")

# Get the text content of the element
response_message_text = response_message_element.text

# Print or use the collected text as needed
print("Collected text:", response_message_text)

# Wait for user input before closing the browser
input("Press Enter to close the browser...")

# Close the browser window
driver.quit()

print(username)






