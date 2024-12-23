from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

# Khởi tạo WebDriver (đảm bảo chỉ định đường dẫn đến driver nếu không có trong PATH)
driver = webdriver.Chrome()

# Thay đổi kích thước cửa sổ trình duyệt
driver.set_window_size(1200, 800)

# Mở trang web
driver.get("http://127.0.0.1:5501/web_ban_sach/front-end/Giao_dien_web%20ban_hang/index.html")

# Chờ trang tải xong
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "onclick_1")))

# Danh sách lưu kết quả
test_results = []

# Vòng lặp qua các phần tử onclick từ 1 đến 15
for i in range(1, 12):
    try:
        # Tạo ID cho phần tử onclick
        onclick_id = f"onclick_{i}"
        
        # Chờ cho phần tử onclick có thể nhấp được
        onclick_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, onclick_id))
        )
        
        # Cuộn đến phần tử trước khi nhấp
        driver.execute_script("arguments[0].scrollIntoView();", onclick_element)
        
        # Nhấp vào phần tử onclick bằng JavaScript
        driver.execute_script("arguments[0].click();", onclick_element)
        
        # Chờ một chút để trang mới tải
        time.sleep(2)
        
        # Kiểm tra URL của trang hiện tại
        current_url = driver.current_url
        
        # Kiểm tra xem URL có chứa "detail_books.html" hay không
        if "detail_books.html" in current_url:
            result = f"Sách {i} đang ở trang chi tiết sách."
        else:
            result = f"Sách {i}: Không phải trang chi tiết sách. URL hiện tại: {current_url}"
        
        # Thêm kết quả vào danh sách
        test_results.append([f"Sách {i}", result])
        
        # Quay lại trang chính
        driver.back()
        
        # Chờ trang chính tải lại
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "onclick_1")))

        # Chờ trước khi nhấp vào sách tiếp theo
        time.sleep(1)
        
    except Exception as e:
        test_results.append([f"Sách {i}", f"Đã xảy ra lỗi: {e}"])

# Đóng driver
driver.quit()

# Tạo DataFrame từ danh sách kết quả
df = pd.DataFrame(test_results, columns=["Sách", "Kết quả"])

# Lưu DataFrame vào file Excel
df.to_excel("chi_tiet.xlsx", index=False)
