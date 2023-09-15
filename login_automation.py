pip install selenium
# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define the URL of the web application
url = "https://example.com/login"

# Initialize the web driver (in this case, we're using Chrome)
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

# Navigate to the login page
driver.get(url)

# Find the username and password input fields and the login button
username_input = driver.find_element(By.ID, "username")
password_input = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

# Enter your login credentials
username_input.send_keys("your_username")
password_input.send_keys("your_password")

# Click the login button to submit the form
login_button.click()

# Wait for the dashboard page to load (you can change the timeout value as needed)
wait = WebDriverWait(driver, 10)
dashboard_element = wait.until(EC.presence_of_element_located((By.ID, "dashboard")))

# Check if the login was successful by verifying the presence of a dashboard element
if dashboard_element:
    print("Login successful!")
else:
    print("Login failed!")

# Close the web browser
driver.quit()
