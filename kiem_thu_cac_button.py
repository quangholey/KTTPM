from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

# Initialize the WebDriver
driver = webdriver.Chrome()  # or webdriver.Firefox() for Firefox

# Create a list to store test results
test_results = []

try:
    # Open the webpage
    driver.get("http://127.0.0.1:5501/web_ban_sach/front-end/Giao_dien_web%20ban_hang/index.html")
    test_results.append(["Open Webpage", "Success"])

    # Test Navigation to Home
    home_link = driver.find_element(By.LINK_TEXT, "Home")
    home_link.click()
    time.sleep(2)  # Wait for the page to load
    test_results.append(["Navigate to Home", "Success"])

    # Test Navigation to "Xem các loại sách"
    books_link = driver.find_element(By.LINK_TEXT, "Xem các loại sách")
    books_link.click()
    time.sleep(2)
    test_results.append(["Navigate to 'Xem các loại sách'", "Success"])

    # Go back to the home page
    driver.back()
    time.sleep(2)  # Wait for the page to load
    test_results.append(["Back to Home Page", "Success"])

    # Test Navigation to "USER"
    user_link = driver.find_element(By.LINK_TEXT, "USER")
    user_link.click()
    time.sleep(2)
    test_results.append(["Navigate to 'USER'", "Success"])

    # Go back to the home page
    driver.back()
    time.sleep(2)  # Wait for the page to load
    test_results.append(["Back to Home Page", "Success"])

    # Test Add to Cart Functionality
    cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "cart_button"))
    )
    cart_button.click()  # Click the cart button to open the modal
    time.sleep(2)  # Wait for the modal to open
    test_results.append(["Add to Cart", "Success"])

    # Test Order Modal
    order_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "dat_hang"))
    )
    order_button.click()
    time.sleep(2)  # Wait for the order modal to open
    test_results.append(["Open Order Modal", "Success"])

    # Click the 'Hủy' button to cancel the order using ID
    cancel_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "Huy"))  # Thay đổi ở đây
    )
    cancel_button.click()  # Click the 'Hủy' button
    time.sleep(2)  # Wait for the modal to close
    test_results.append(["Cancel Order", "Success"])

finally:
    # Close the WebDriver
    driver.quit()

    # Create DataFrame from the results and save to Excel
    df = pd.DataFrame(test_results, columns=["Test", "Result"])
    df.to_excel("test_results.xlsx", index=False)

