# OrangeHRM_UIAutomationFramework

Writing and automating test cases for Open Source OrangeHRM HR Software. The UI Automation framework is based on the Page Object Model (POM) design pattern and uses Selenium, Python, Pytest, Git, and HTML Reports.

This project implements the Page Object Model design pattern using Selenium WebDriver with Pytest, written in Python, and utilizes Pytest assertions.

HTML Reports are generated after test execution using the `pytest-html` plugin.

## Functionality
- **Login with Valid Credentials**: Automates the login process by testing valid user credentials.
- **Dashboard Navigation**: Tests the navigation from the dashboard to the "My Info" tab.
- **My Info Page Verification**: Ensures the My Info page loads successfully, validating the page URL.
- **Personal Details Entry**: Automates filling out personal details such as first name, middle name, last name, employee ID, and driver's license information.
- **File Attachment Upload**: Tests file uploading functionality by attaching files (e.g.,.png, PDF) to the My Info page.

## Technology Stack
- **Language**: Python
- **Web Automation**: Selenium WebDriver
- **Testing Framework**: Pytest
- **Continuous Integration**: GitHub Actions
- **Reporting**: pytest-html
- **Design Pattern**: Page Object Model (POM)

## Prerequisites
- Python 3.x installed
- Google Chrome browser installed
- ChromeDriver (ensure the correct version of ChromeDriver is used, corresponding to your Chrome version)
- Git
- GitHub Actions (for CI)

## Page Object Model (POM)

Page Object Model (POM) is a design pattern in Selenium that creates an object repository for storing all web elements. It helps reduce code duplication and improves test case maintenance.

In POM, each web page of an application is considered as a class file. Each class file contains only the web page elements. Using these elements, you can perform operations on the website under test.

### Why Page Object Model?

1. Helps with easy maintenance.
2. Reusability of code.
3. Readability and reliability of scripts.
4. Provides structure to the automation framework.

## Test Framework

Selenium is a free (open-source) automated testing framework used to validate web applications across different browsers and platforms. 

**Pytest** is a testing framework written in Python. It makes it easy to write small tests, yet scales to support complex functional testing. All functional tests are created using Pytest `@pytest.mark.usefixtures` in the `tests` directory.

**Pytest assertions** have been used for all the test validations.

**pytest-html** has been used for reporting, and the reports are generated after every run at the following path: `/reports/report.html`. The report can be opened in any web browser to see detailed results of each test run.

### Why Pytest with Selenium for Framework?

1. Easy maintainability and reusability.
2. Simple and readable annotations in Pytest.
3. Easy to group and organize test cases in Pytest.
4. Pytest allows for parallel test execution using plugins.
5. HTML reports can be generated with `pytest-html`.
6. Both Selenium and Pytest are open-source tools with great community support.

### Alternative Options Available for Frontend Automation:

- Cucumber with Selenium
- Playwright with Python
- WebdriverIO
- Cypress
- Serenity BDD

### Pre-requisite:

- Python 3.x installed.
- Chrome browser - latest version installed.
- ChromeDriver - ensure that the correct version is installed, corresponding to the version of Chrome.
- Pytest and Selenium WebDriver dependencies installed.
- Git installed and configured.
## Setup
1. Install and configure Python 3
Ensure that Python 3 is installed on your machine. You can download it from [here](https://www.python.org/downloads/). After installation, ensure `pip` is also installed.'
2. Setup your IDE
You can use any Python-compatible IDE like **PyCharm**, **VSCode**, or **IntelliJ IDEA**. Configure the IDE to point to your Python 3 interpreter.
3. Import cloned repository as project
Clone the repository using Git, and import it into your IDE as a project:

```bash
git clone https://github.com/your-username/orangehrm-selenium.git
cd orangehrm-selenium

### Clone the Repository:

```bash
git clone https://github.com/your-username/orangehrm-selenium.git
cd orangehrm-selenium
