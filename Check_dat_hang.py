from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

# Danh sách lưu kết quả
test_results = []

def open_cart(driver):
    """Function to open the cart modal."""
    try:
        # Wait for the cart button to be clickable
        cart_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "cart_button"))
        )
        cart_button.click()  # Click the cart button to open the modal
        time.sleep(2)  # Wait for the modal to open
        test_results.append(["Mở giỏ hàng", "Thành công"])
    except Exception as e:
        test_results.append(["Mở giỏ hàng", f"Lỗi: {e}"])

def click_order_button(driver):
    """Function to click the 'Đặt hàng' button in the cart modal."""
    try:
        # Wait for the 'Đặt hàng' button to be clickable
        order_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "dat_hang"))
        )
        order_button.click()  # Click the 'Đặt hàng' button
        time.sleep(2)  # Wait for the order modal to open
        test_results.append(["Nhấn Đặt hàng", "Thành công"])
    except Exception as e:
        test_results.append(["Nhấn Đặt hàng", f"Lỗi: {e}"])

def fill_order_form(driver):
    """Function to fill in the order form."""
    try:
        # Select the first province
        province_select = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "province"))
        )
        province_select.click()
        first_province_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id='province']/option[not(@disabled)]"))
        )
        first_province_option.click()
        time.sleep(1)

        # Select the first district
        district_select = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "district"))
        )
        district_select.click()
        first_district_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id='district']/option[not(@disabled)]"))
        )
        first_district_option.click()
        time.sleep(1)

        # Select the first ward
        ward_select = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "ward"))
        )
        ward_select.click()
        first_ward_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id='ward']/option[not(@disabled)]"))
        )
        first_ward_option.click()
        time.sleep(1)

        # Fill in the address
        address_input = driver.find_element(By.ID, "address")
        address_input.send_keys("ap1")
        time.sleep(1)

        test_results.append(["Điền thông tin đơn hàng", "Thành công"])
    except Exception as e:
        test_results.append(["Điền thông tin đơn hàng", f"Lỗi: {e}"])

def click_apply_code(driver):
    """Function to click the 'Xác nhận đặt hàng' button in the order modal."""
    try:
        # Wait for the 'Áp mã' button to be clickable
        apply_code_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "xac_nhan_dat_hang"))
        )
        apply_code_button.click()  # Click the 'Áp mã' button
        time.sleep(2)  # Wait for any resulting action
        test_results.append(["Nhấn Áp mã", "Thành công"])
    except Exception as e:
        test_results.append(["Nhấn Áp mã", f"Lỗi: {e}"])

def click_cancel_button(driver):
    """Function to click the 'Hủy' button in the order modal."""
    try:
        # Wait for the 'Hủy' button to be clickable
        cancel_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "Huy"))
        )
        cancel_button.click()  # Click the 'Hủy' button
        time.sleep(2)  # Wait for the modal to close
        test_results.append(["Nhấn Hủy", "Thành công"])
    except Exception as e:
        test_results.append(["Nhấn Hủy", f"Lỗi: {e}"])

# Example usage
if __name__ == "__main__":
    # Initialize the WebDriver
    driver = webdriver.Chrome()  # or webdriver.Firefox() for Firefox

    try:
        # Open the webpage
        driver.get("http://127.0.0.1:5501/web_ban_sach/front-end/Giao_dien_web%20ban_hang/index.html")

        # Open the cart modal
        open_cart(driver)

        # Click the 'Đặt hàng' button
        click_order_button(driver)

        # Fill in the order form
        fill_order_form(driver)

        # Click the 'Áp mã' button
        click_apply_code(driver)

        # You can add more tests here after applying the code

        # Optionally, click the cancel button
        click_cancel_button(driver)

    finally:
        # Save the results to an Excel file
        df = pd.DataFrame(test_results, columns=["Action", "Status"])
        df.to_excel("check_dat_hang.xlsx", index=False)

        # Close the WebDriver
        driver.quit()
