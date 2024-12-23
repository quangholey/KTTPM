import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import UnexpectedAlertPresentException, TimeoutException
import time

# Đường dẫn đến ChromeDriver
CHROME_DRIVER_PATH = r"C:\Users\QUANGHONEY\Downloads\chromedriver-win64 (1)\chromedriver-win64\chromedriver.exe"
service = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service)

# Đọc các test case từ file Excel sử dụng pandas
df = pd.read_excel(r'C:\Users\QUANGHONEY\Desktop\Code\Python_flask_api\web_ban_sach\register_tests.xlsx', engine='openpyxl')

# Thay thế NaN bằng chuỗi rỗng hoặc giá trị mặc định nếu cần
df.fillna('', inplace=True)  # Thay toàn bộ giá trị NaN bằng chuỗi rỗng

# Vòng lặp kiểm tra đăng ký cho từng tài khoản
for index, account in df.iterrows():
    try:
        # Kiểm tra nếu có dữ liệu thiếu ở bất kỳ trường nào
        required_fields = ['name', 'address', 'phone_numbers', 'account_user', 'password_user', 'confirm_password']
        if any(account[col] == '' for col in required_fields):
            df.at[index, 'result'] = 'failed: missing fields'
            continue

        # Kiểm tra nếu password và confirm_password không khớp
        if account['password_user'] != account['confirm_password']:
            df.at[index, 'result'] = 'failed: password mismatch'
            continue

        # Mở trang đăng ký ở tab mới
        driver.execute_script("window.open('http://127.0.0.1:5501/web_ban_sach/front-end/UI-EcommerceApp/register.html');")
        
        # Chuyển đến tab mới
        driver.switch_to.window(driver.window_handles[-1])

        # Đợi cho phần tử nhập liệu xuất hiện
        wait = WebDriverWait(driver, 10)
        name_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='name']")))
        name_field.clear()
        name_field.send_keys(account['name'])

        address_field = driver.find_element(By.XPATH, "//input[@placeholder='address']")
        address_field.clear()
        address_field.send_keys(account['address'])

        phone_field = driver.find_element(By.XPATH, "//input[@placeholder='phone_numbers']")
        phone_field.clear()
        phone_field.send_keys(account['phone_numbers'])

        username_field = driver.find_element(By.XPATH, "//input[@placeholder='account_user']")
        username_field.clear()
        username_field.send_keys(account['account_user'])

        password_field = driver.find_element(By.XPATH, "//input[@placeholder='password_user']")
        password_field.clear()
        password_field.send_keys(account['password_user'])

        confirm_password_field = driver.find_element(By.XPATH, "//input[@placeholder='confirm_password']")
        confirm_password_field.clear()
        confirm_password_field.send_keys(account['confirm_password'])

        # Gửi form đăng ký
        register_button = driver.find_element(By.XPATH, "//button[text()='Register']")
        register_button.click()

        # Kiểm tra cảnh báo nếu có
        try:
            WebDriverWait(driver, 3).until(EC.alert_is_present())
            alert = driver.switch_to.alert
            alert_text = alert.text
            alert.accept()
            df.at[index, 'result'] = f'failed: {alert_text}'
        except TimeoutException:
            # Không có alert, tiếp tục kiểm tra URL
            current_url = driver.current_url
            if "login" in current_url:  # Nếu chuyển hướng đến trang login
                df.at[index, 'result'] = 'pass'
            else:
                df.at[index, 'result'] = 'failed: no redirect to login'

    except Exception as e:
        print(f"Error for account {account['account_user']}: {str(e)}")
        df.at[index, 'result'] = f'failed: {str(e)}'

    finally:
        # Đóng tab hiện tại và chuyển lại về tab chính
        if len(driver.window_handles) > 1:
            driver.close()
            driver.switch_to.window(driver.window_handles[0])

# Ghi lại kết quả vào file Excel
df.to_excel(r'C:\Users\QUANGHONEY\Desktop\Code\Python_flask_api\web_ban_sach\RegisterTestResults.xlsx', index=False, engine='openpyxl')

# Đóng trình duyệt sau khi hoàn tất
driver.quit()
