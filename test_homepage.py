
# Importing necessary modules


import pytest

from TestLocators.HomepageLocators import Locators
from TestData.HomepageData import Homepage
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Define a test class
class Test_OrangeHRM:

    # Define a fixture for setting up and tearing down the test environment
    @pytest.fixture
    # Define a booting function
    def booting_function(self):
        # Initialize the Firefox WebDriver using GeckoDriverManager
        self.driver=webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        # Navigate to the URL specified in the Homepage data
        self.driver.get(Homepage().url)
        # Maximize the browser window
        self.driver.maximize_window()
        # Set up WebDriverWait to wait for elements to be available
        self.wait=WebDriverWait(self.driver,10)

        # Yield control back to the test function
        yield
        # Close the browser window after the test is complete
        self.driver.close()


    # Define a test for forgot password link validation on login page
    def test_TC_PIM_01(self,booting_function):
        try:

            # Locate the 'Forgot Password' button and click it
            forgot_password=self.wait.until(EC.element_to_be_clickable((By.XPATH,Locators().forgot_password_button)))
            forgot_password.click()


            # Assert that the current URL is the reset password URL
            assert self.driver.current_url==Homepage().reset_password_url

            # Locate the username input box and enter the username from Homepage data

            username_input_box=self.wait.until(EC.visibility_of_element_located((By.XPATH,Locators().username_input_box2)))
            username_input_box.send_keys(Homepage().username)

            # Locate the 'Reset Password' button and click it

            reset_password_button=self.wait.until(EC.element_to_be_clickable((By.XPATH,Locators().reset_password_button)))
            reset_password_button.click()

            # Assert that the current URL is the reset password link URL

            assert self.driver.current_url==Homepage().reset_password_link_url


            # Locate the element showing the success message and verify its text and visibility
            reset_password_link=self.wait.until(EC.visibility_of_element_located((By.XPATH,Locators.rest_password_link)))
            assert reset_password_link.text=="Reset Password link sent successfully"
            assert reset_password_link.is_displayed()

            # Print a success message indicating the reset password link was sent successfully
            print("SUCCESS : Rest password link sent successfully")

        except NoSuchElementException as e:
            # Catch exceptions related to elements not being found and print the exception message
            print(e)



# Define  a test for header validation of admin page
    def test_TC_PIM_02(self,booting_function):
        try:

            # Locate the username input box and enter the username from the Homepage object
            username = self.wait.until(EC.visibility_of_element_located((By.NAME, Locators().username_input_box)))
            username.send_keys(Homepage().username)

            # Locate the password input box and enter the password from the Homepage object
            password = self.wait.until(EC.visibility_of_element_located((By.NAME, Locators().password_input_box)))
            password.send_keys(Homepage().password)

            # Locate and click the submit button to log in
            submit_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators().submit_button)))
            submit_button.click()

            # Locate and click the Admin button to navigate to the Admin section
            admin_button=self.wait.until(EC.element_to_be_clickable((By.XPATH,Locators().admin_button)))
            admin_button.click()

            # Assert that the page title is "OrangeHRM" to confirm successful navigation
            assert self.driver.title == "OrangeHRM"

            # Locate the User Management option and verify it is visible and enabled
            user_management=self.wait.until(EC.visibility_of_element_located((By.XPATH,Locators().user_management_option)))
            # Check if the User Management option is displayed
            assert user_management.is_displayed()
            # Check if the User Management option is enabled
            assert user_management.is_enabled()
            print("SUCCESS : User Management option is displayed")

            # Locate the Job option and verify it is visible and enabled
            job_option=self.wait.until(EC.visibility_of_element_located((By.XPATH,Locators().job_option)))
            # Check if the Job option is displayed
            assert job_option.is_displayed()
            # Check if the Job option is enabled
            assert job_option.is_enabled()
            print("SUCCESS : Job option is displayed")

            # Locate the Organization option and verify it is visible and enabled
            organization_option=self.wait.until(EC.visibility_of_element_located((By.XPATH,Locators().organization_option)))
            # Check if the Organization option is displayed
            assert organization_option.is_displayed()
            # Check if the Organization option is enabled
            assert organization_option.is_enabled()
            print("SUCCESS : Organization option is displayed")

            # Locate the Qualification option and verify it is visible and enabled
            qualification_option=self.wait.until(EC.visibility_of_element_located((By.XPATH,Locators().qualification_option)))
            # Check if the Qualification option is displayed
            assert qualification_option.is_displayed()
            # Check if the Qualification option is enabled
            assert qualification_option.is_enabled()
            print("SUCCESS : Qualification option is displayed")

            # Locate the Nationalities option and verify it is visible and enabled
            nationalities_option=self.wait.until(EC.visibility_of_element_located((By.XPATH,Locators().nationalities_option)))
            # Check if the Nationalities option is displayed
            assert nationalities_option.is_displayed()
            # Check if the Nationalities option is enabled
            assert nationalities_option.is_enabled()
            print("SUCCESS : Nationalities option is displayed ")

            # Locate the Corporate Banking option and verify it is visible and enabled
            corporate_banking_option = self.wait.until(EC.visibility_of_element_located((By.XPATH, Locators().corporate_banking_option)))
            # Check if the Corporate Banking option is displayed
            assert corporate_banking_option.is_displayed()
            # Check if the Corporate Banking option is enabled
            assert corporate_banking_option.is_enabled()
            print("SUCCESS : Corporate Banking option is displayed ")

            # Locate and click the 'More' option to reveal additional options
            more_option=self.wait.until(EC.visibility_of_element_located((By.XPATH,Locators().more_option)))
            more_option.click()

            # Locate the Configuration option and verify it is visible and enabled
            configuration_option=self.wait.until(EC.visibility_of_element_located((By.XPATH,Locators().configuration_option)))
            # Check if the Configuration option is displayed
            assert configuration_option.is_displayed()
            # Check if the Configuration option is enabled
            assert configuration_option.is_enabled()
            print("SUCCESS : Configuration option is displayed")



        except NoSuchElementException as e:
            # Catch exceptions related to elements not being found and print the exception message
            print(e)



# Define a test for Main Menu validation on Admin page

    def test_TC_PIM_03(self,booting_function):
        try:

            # Locate the username input box, wait until it is visible, and enter the username from the Homepage data
            username = self.wait.until(EC.visibility_of_element_located((By.NAME, Locators().username_input_box)))
            username.send_keys(Homepage().username)

            # Locate the password input box, wait until it is visible, and enter the password from the Homepage data
            password = self.wait.until(EC.visibility_of_element_located((By.NAME, Locators().password_input_box)))
            password.send_keys(Homepage().password)

            # Locate the submit button, wait until it is clickable, and click it to log in
            submit_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators().submit_button)))
            submit_button.click()

            # Verify the visibility and functionality of the Admin option
            admin_option=self.wait.until(EC.visibility_of_element_located((By.XPATH,Locators().admin_button)))
            # Check if the Admin option is visible
            assert admin_option.is_displayed()
            # Check if the Admin option is enabled
            assert admin_option.is_enabled()
            print("SUCCESS : Admin option is displayed")

            # Verify the visibility and functionality of the PIM option
            pim_option=self.wait.until(EC.visibility_of_element_located((By.XPATH,Locators().pim_option)))
            # Check if the PIM option is visible
            assert pim_option.is_displayed()
            # Check if the PIM option is enabled
            assert pim_option.is_enabled()
            print("SUCCESS : PIM option is displayed")

            # Verify the visibility and functionality of the Leave option
            leave_option=self.wait.until(EC.visibility_of_element_located((By.XPATH,Locators().leave_option)))
            # Check if the Leave option is visible
            assert leave_option.is_displayed()
            # Check if the Leave option is enabled
            assert leave_option.is_enabled()
            print("SUCCESS : Leave option is displayed")

            # Verify the visibility and functionality of the Time option
            time_option=self.wait.until(EC.visibility_of_element_located((By.XPATH,Locators().time_option)))
            # Check if the Time option is visible
            assert time_option.is_displayed()
            # Check if the Time option is enabled
            assert time_option.is_enabled()
            print("SUCCESS : Time option is displayed")

            # Verify the visibility and functionality of the Recruitment option
            recruitment_option=self.wait.until(EC.visibility_of_element_located((By.XPATH,Locators().recruitment_option)))
            # Check if the Recruitment option is visible
            assert recruitment_option.is_displayed()
            # Check if the Recruitment option is enabled
            assert recruitment_option.is_enabled()
            print("SUCCESS : Recruitment option is displayed")

            # Verify the visibility and functionality of the My Info option
            my_info_option=self.wait.until(EC.visibility_of_element_located((By.XPATH,Locators().my_info_option)))
            # Check if the My Info option is visible
            assert my_info_option.is_displayed()
            # Check if the My Info option is enabled
            assert my_info_option.is_enabled()
            print("SUCCESS : My Info option is displayed")

            # Verify the visibility and functionality of the Performance option
            performance_option=self.wait.until(EC.visibility_of_element_located((By.XPATH,Locators().performance_option)))
            # Check if the Performance option is visible
            assert performance_option.is_displayed()
            # Check if the Performance option is enabled
            assert performance_option.is_enabled()
            print("SUCCESS : Performance option is displayed")

            # Verify the visibility and functionality of the Dashboard option
            dashboard_option=self.wait.until(EC.visibility_of_element_located((By.XPATH,Locators().dashboard_option)))
            # Check if the Dashboard option is visible
            assert dashboard_option.is_displayed()
            # Check if the Dashboard option is enabled
            assert dashboard_option.is_enabled()
            print("SUCCESS : Dashboard option is displayed")

            # Verify the visibility and functionality of the Directory option
            directory_option=self.wait.until(EC.visibility_of_element_located((By.XPATH,Locators().directory_option)))
            # Check if the Directory option is visible
            assert directory_option.is_displayed()
            # Check if the Directory option is enabled
            assert directory_option.is_enabled()
            print("SUCCESS : Directory option is displayed")

            # Verify the visibility and functionality of the Maintenance option
            maintenance_option=self.wait.until(EC.visibility_of_element_located((By.XPATH,Locators().maintenance_option)))
            # Check if the Maintenance option is visible
            assert maintenance_option.is_displayed()
            # Check if the Maintenance option is enabled
            assert maintenance_option.is_enabled()
            print("SUCCESS : Maintenance option is displayed")

            # Verify the visibility and functionality of the Claim option
            claim_option=self.wait.until(EC.visibility_of_element_located((By.XPATH,Locators().claim_option)))
            # Check if the Claim option is visible
            assert claim_option.is_displayed()
            # Check if the Claim option is enabled
            assert claim_option.is_enabled()
            print("SUCCESS : Claim option is displayed")

            # Verify the visibility and functionality of the Buzz option
            buzz_option=self.wait.until(EC.visibility_of_element_located((By.XPATH,Locators().buzz_option)))
            # Check if the Buzz option is visible
            assert buzz_option.is_displayed()
            # Check if the Buzz option is enabled
            assert buzz_option.is_enabled()
            print("SUCCESS : Buzz option is displayed")


        except NoSuchElementException as e:
            # Catch and print exceptions related to elements not being found
            print(e)














