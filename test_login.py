import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Đường dẫn đến ChromeDriver
CHROME_DRIVER_PATH = r"C:\Users\QUANGHONEY\Downloads\chromedriver-win64 (1)\chromedriver-win64\chromedriver.exe"
service = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service)

# Đọc các test case từ file Excel sử dụng pandas
df = pd.read_excel(r'C:\Users\QUANGHONEY\Desktop\Code\Python_flask_api\web_ban_sach\login_tests.xlsx', engine='openpyxl')

# Thay thế NaN bằng chuỗi rỗng hoặc giá trị mặc định nếu cần
df['username'].fillna('', inplace=True)
df['password'].fillna('', inplace=True)
df['role'].fillna('', inplace=True)
df['result'].fillna('failed', inplace=True)  # Đảm bảo cột 'result' có giá trị mặc định

# Vòng lặp kiểm tra đăng nhập cho từng tài khoản
for index, account in df.iterrows():
    try:
        # Kiểm tra nếu có dữ liệu thiếu ở bất kỳ trường nào
        if account['username'] == '' or account['password'] == '' or account['role'] == '':
            df.at[index, 'result'] = 'failed'  # Nếu có trường trống, gán kết quả là 'failed'
            continue

        # Mở trang login ở tab mới
        driver.execute_script("window.open('http://127.0.0.1:5501/web_ban_sach/front-end/UI-EcommerceApp/login.html');")
        
        # Chuyển đến tab mới
        driver.switch_to.window(driver.window_handles[-1])

        # Đợi cho phần tử username xuất hiện
        wait = WebDriverWait(driver, 10)
        username_field = wait.until(EC.presence_of_element_located((By.ID, 'user')))
        
        # Điền thông tin đăng nhập
        username_field.clear()
        username_field.send_keys(account['username'])

        password_field = wait.until(EC.presence_of_element_located((By.ID, 'pass')))
        password_field.clear()
        password_field.send_keys(account['password'])

        login_button = driver.find_element(By.ID, 'login')
        login_button.click()

        # Đợi một chút để kiểm tra kết quả đăng nhập
        time.sleep(3)

        # Kiểm tra nếu có cảnh báo
        try:
            alert = Alert(driver)
            alert_text = alert.text
            print(f"Alert text: {alert_text}")

            # Chấp nhận cảnh báo và đánh dấu kết quả là "failed"
            alert.accept()
            df.at[index, 'result'] = 'failed'
            continue

        except Exception as e:
            print("No alert found.")

        # Kiểm tra URL sau khi đăng nhập
        current_url = driver.current_url

        # Kiểm tra nếu đăng nhập thành công
        if account['role'] == 'admin' and "NiceAdmin" in current_url:
            df.at[index, 'result'] = 'pass'
        elif account['role'] == 'user' and "Giao_dien_web" in current_url:
            df.at[index, 'result'] = 'pass'
        else:
            df.at[index, 'result'] = 'failed'
            print(f"failed for {account['username']}, current URL: {current_url}")

    except Exception as e:
        print(f"Error for account {account['username']}: {str(e)}")
        df.at[index, 'result'] = 'failed'

    # Đóng tab hiện tại và chuyển lại về tab chính (nếu cần)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

# Ghi lại kết quả vào file Excel
df.to_excel(r'C:\Users\QUANGHONEY\Desktop\Code\Python_flask_api\web_ban_sach\LoginTest.xlsx', index=False, engine='openpyxl')

# Đóng trình duyệt sau khi hoàn tất
driver.quit()
