# Analystt.ai_assessment
I have developed a simple automated test script using Python and a testing to automate the login process of a sample web application. 


# Analystt.ai Assessment

This project contains a simple automated test script written in Python using Selenium to automate the login process of a sample web application.

## Prerequisites

1. Install Python (version 3.6 or higher).
2. Install Selenium by running the following command in your terminal:
   ```bash
   pip install selenium
   ```
3. Download the appropriate WebDriver for your browser (e.g., ChromeDriver for Google Chrome) and ensure it is added to your system's PATH or specify its location in the script.

## Usage

1. Update the `login_automation.py` script with the correct URL, username, password, and WebDriver path:
   - Replace `https://example.com/login` with the URL of the login page.
   - Replace `your_username` and `your_password` with valid credentials.
   - Update `/path/to/chromedriver` with the path to your WebDriver executable.

2. Run the script using the following command:
   ```bash
   python login_automation.py
   ```

3. The script will:
   - Open the login page in a browser.
   - Enter the provided username and password.
   - Attempt to log in and verify if the login was successful by checking for the presence of a dashboard element.

## Output

- If the login is successful, the script will print:
  ```
  Login successful!
  ```
- If the login fails, the script will print:
  ```
  Login failed!
  ```

## Notes

- Ensure the WebDriver version matches your browser version.
- Modify the element locators (`By.ID`) in the script if the web application's structure changes.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

## Contact

- **Email**: gauravupadhayay9801@gmail.com  
- **GitHub**: [grajrb](https://github.com/grajrb)  
- **LinkedIn**: [Gaurav Raj](https://www.linkedin.com/in/gaurav-raj-095a8a129/)