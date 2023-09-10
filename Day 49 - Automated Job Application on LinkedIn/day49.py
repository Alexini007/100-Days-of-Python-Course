from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.common.exceptions import NoSuchElementException
import time
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3708706274&distance=25"
           ".0&f_AL=true&geoId=102257491&keywords=python%20developer&sortBy=R")

time.sleep(3)
cookies = driver.find_element(By.CSS_SELECTOR, value='button[action-type="DENY"]')
cookies.click()

time.sleep(2)
signin_button = driver.find_element(By.LINK_TEXT, value="Sign in")
signin_button.click()

time.sleep(1)
username = driver.find_element(By.ID, value="username")
username.send_keys("***")

password = driver.find_element(By.ID, value="password")
password.send_keys("***")

password.send_keys(Keys.ENTER)
time.sleep(5)

# Here we are only saving the job offers
listings = driver.find_elements(By.CSS_SELECTOR, value=".job-card-container--clickable")
for listing in listings:
    print("Opening Listing")
    listing.click()
    time.sleep(2)
    save_button = driver.find_element(By.CLASS_NAME, value="jobs-save-button")
    save_button.click()
    print("Saved")

# Here we are applying for job offers
# def abort_application():
#     # Click Close Button
#     close_button = driver.find_element(By.CLASS_NAME, value="artdeco-modal__dismiss")
#     close_button.click()
#     time.sleep(2)
#     # Click Discard Button
#     discard_button = driver.find_elements(By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
#     discard_button.click()
#
#
# for listing in listings:
#     print("Opening Listing")
#     listing.click()
#     time.sleep(2)
#     try:
#         # Click Apply Button
#         apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
#         apply_button.click()
#
#         # Insert Phone Number
#         # Find an <input> element where the id contains phoneNumber
#         time.sleep(5)
#         phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
#         if phone.text == "":
#             phone.send_keys(PHONE)
#
#         # Check the Submit Button
#         submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
#         if submit_button.get_attribute("data-control-name") == "continue_unify":
#             abort_application()
#             print("Complex application, skipped.")
#             continue
#         else:
#             # Click Submit Button
#             print("Submitting job application")
#             submit_button.click()
#
#         time.sleep(2)
#         # Click Close Button
#         close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
#         close_button.click()
#
#     except NoSuchElementException:
#         abort_application()
#         print("No application button, skipped.")
#         continue

# driver.quit()