import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Đường dẫn đến ChromeDriver
CHROME_DRIVER_PATH = r"C:\Users\QUANGHONEY\Downloads\chromedriver-win64 (1)\chromedriver-win64\chromedriver.exe"
service = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service)

# Tạo DataFrame để lưu kết quả
results = {
    'product_id': [],
    'result': []
}

# Danh sách các sản phẩm để kiểm tra
product_ids = [1, 2, 3]  # Thay đổi ID sản phẩm theo nhu cầu

# Vòng lặp kiểm tra thêm vào giỏ hàng cho từng sản phẩm
for product_id in product_ids:
    try:
        # Mở trang sản phẩm
        driver.get("http://127.0.0.1:5501/web_ban_sach/front-end/Giao_dien_web%20ban_hang/index.html")

        # Chờ 2 giây để trang tải xong
        time.sleep(2)

        # Đợi cho phần tử nút "Thêm vào giỏ hàng" xuất hiện
        wait = WebDriverWait(driver, 10)
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.ID, f"btn_{product_id}")))

        # Kiểm tra số lượng trong giỏ hàng trước khi thêm
        cart_count_before = wait.until(EC.visibility_of_element_located((By.ID, "cart-count")))
        initial_count = int(cart_count_before.text)
        print(f"Before adding product ID {product_id}: {initial_count}")  # In ra số lượng trước khi thêm

        # Cuộn đến nút "Thêm vào giỏ hàng"
        driver.execute_script("arguments[0].scrollIntoView();", add_to_cart_button)

        # Nhấp vào nút "Thêm vào giỏ hàng" bằng JavaScript
        driver.execute_script("arguments[0].click();", add_to_cart_button)

        # Đợi một chút để alert xuất hiện
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert_text = alert.text
        print(f"Alert Text: {alert_text}")  # In ra nội dung alert
        alert.accept()  # Nhấn OK để đóng alert

        # Đợi một chút để kiểm tra số lượng trong giỏ hàng
        time.sleep(3)

        # Kiểm tra số lượng trong giỏ hàng sau khi thêm
        cart_count_after = wait.until(EC.visibility_of_element_located((By.ID, "cart-count")))
        final_count = int(cart_count_after.text)
        print(f"After adding product ID {product_id}: {final_count}")  # In ra số lượng sau khi thêm

        # So sánh số lượng
        if final_count > initial_count:
            results['product_id'].append(product_id)
            results['result'].append('pass')
        else:
            results['product_id'].append(product_id)
            results['result'].append('failed')
            print(f"Add to cart failed for product ID {product_id}, cart count: {final_count}")

    except Exception as e:
        print(f"Error for product ID {product_id}: {str(e)}")
        results['product_id'].append(product_id)
        results['result'].append('failed')

# Chuyển kết quả sang DataFrame và ghi vào file Excel
results_df = pd.DataFrame(results)
results_df.to_excel('AddToCartTestResults.xlsx', index=False, engine='openpyxl')

# Đóng trình duyệt sau khi hoàn tất
driver.quit()