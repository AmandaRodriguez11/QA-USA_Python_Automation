from selenium.webdriver.common.by import By


class HomePageAround:
    # The Add button locator
    add_new_place_button = (By.CLASS_NAME, 'profile__add-button')
    # The Name field locator
    name_field = (By.NAME, 'name')
    # The Link-to-the-image field locator
    link_to_picture_field = (By.NAME, 'link')
    # The Save button locator
    save_button = (By.XPATH, ".//form[@name='new-card']/button[text()='Save']")

    def __init__(self, driver):
        self.driver = driver

    # The method clicks on the Add button
    def click_add_new_place_button(self):
        self.driver.find_element(*self.add_new_place_button).click()

    # The method enters the name of the new place
    def set_name(self):
        new_title = "New Place"
        self.driver.find_element(*self.name_field).send_keys(new_title)

    # The method enters a link to the image
    def set_link_to_picture_field(self):
        self.driver.find_element(*self.link_to_picture_field).send_keys("Link to the image")

    # The method clicks on the Save button
    def click_save_button(self):
        self.driver.find_element(*self.save_button).click()

    # The step to add a new placehmhm

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get(" SERVER URL ")

# Pause execution for 2 seconds to allow the page to load fully
time.sleep(2)

# Find the FROM field and fill it in
driver...

# Find the TO field and fill it in
driver...

time.sleep(2)

# Find the "Call a taxi" button and click on it
driver...

# Add an explicit wait for the field to load
WebDriverWait(...).until(...)

# Write a comment to the driver
driver...

time.sleep(2)

# Check that your comment is what you expect it to be
assert ...

driver.quit()
mport time

from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
# Replace our link with your own server link here
driver.get("https://cnt-58f226c9-c4cf-45ff-bc0e-36185cc797fa.containerhub.tripleten-services.com/")

# Pause execution for 2 seconds to allow the page to load fully
time.sleep(2)

# Find the logo element using its CSS Selector
element = driver.find_element(By.CSS_SELECTOR, "img.logo-image")
# Initialize a new instance of the Chrome WebDriver
driver = webdriver.Chrome()

# Open the specified URL in the browser
driver.get(" SERVER URL ")

# Pause execution for 2 seconds to allow the page to load fully
time.sleep(2)

# Find the FROM input field and TO input field using their IDs
from_field = driver...
to_field = driver...

# Test the placeholder attribute for each input field to ensure they display the correct text
assert ...
assert ...

# Close the browser and end the WebDriver session
driver...
 Initialize a new instance of the Chrome WebDriver
driver = webdriver.Chrome()

# Open the specified URL in the browser
driver.get(" SERVER URL ")

# Pause execution for 2 seconds to allow the page to load fully
time.sleep(2)

# Find all elements on the page using an XPath selector
elements = driver...

# Check that the number of elements found is greater than 1 by using len()
...

# Close the browser and end the WebDriver session
driver...
# Initialize a new instance of the Chrome WebDriver
driver = webdriver.Chrome()

# Open the specified URL in the browser
driver.get(" SERVER URL ")

# Pause execution for 2 seconds to allow the page to load fully
time.sleep(2)

# Find the FROM input field and TO input field using their IDs
from_field = driver...
to_field = driver...

# Test the placeholder attribute for each input field to ensure they display the correct text
assert ...
assert ...

# Close the browser and end the WebDriver session
driver...
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get(" SERVER URL ")

# Pause execution for 2 seconds to allow the page to load fully
time.sleep(2)

# Find the FROM field and fill it in
driver...

# Find the TO field and fill it in
driver...

time.sleep(2)

# Get the text from "Fastest" mode
mode = ...

time.sleep(2)

# Assert that the text of the mode variable is "Fastest"
assert ...

driver.quit()

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=en")

time.sleep(2)

# Find the Email field and fill it in
...

# Find the Password field and fill it in
...

# Find the Login button and click on it
...

# Add an explicit wait for the page to load
...

# Find the footer
element = ...

# Scroll the footer into view
driver.execute_script(...)

time.sleep(3)

# Check that the footer contains the string 'Around'
assert ...

driver.quit()
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=en")

time.sleep(2)

# Find the Email field and fill it in
...

# Find the Password field and fill it in
...

# Find the Login button and click on it
...

# Add an explicit wait for the page to load
...

# Find the footer
element = ...

# Scroll the footer into view
driver.execute_script(...)

time.sleep(3)

# Check that the footer contains the string 'Around'
assert ...

driver.quit()

# Print the found element to the console
print(element)
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

# Open the Urban Routes home page
driver...

# Check url contains tripleten-services.com
assert ...

# Close the browser
driver...

from selenium import webdriver

driver = webdriver.Chrome() # create Chrome driver
driver.maximize_window() # Full screen mode

driver.get('https://google.com/')  #navigate to the url
current_url = driver.current_url   # get current url
assert 'google.com' in driver.current_url # verify if google.com in the current url

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

# Open the Urban Routes home page
driver.get("tripleten-services.com")

# Check url contains tripleten-services.com
assert 'tripleten-services.com'

# Close the browser
driver.quit()
# Close the browser and end the WebDriver session
driver.quit()
