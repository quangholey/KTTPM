# import pandas as pd
# import openpyxl
# # Dữ liệu test case
# data = {
#     'username': ['admin', 'quang', 'wronguser', '', 'a'],
#     'password': ['admin123', '1', None, 'a', ''],
#     'role': ['admin', 'user', None, 'user', 'user'],
#     'result': [None, None, None, None, None]
# }

# # Tạo DataFrame từ dữ liệu trên
# df = pd.DataFrame(data)

# # Ghi DataFrame vào file Excel
# df.to_excel('login_tests.xlsx', index=False, engine='openpyxl')

# print("Test case file created successfully!")




import pandas as pd

# Dữ liệu test case
data = {
    "name": ["Doe", "Jane Smith", "Alice Brown", "Bob White", "Invalid User", "No Address"],
    "address": ["123 Main St", "456 Oak Rd", "789 Pine Ave", "321 Elm St", "", ""],
    "phone_numbers": ["1234567890", "9876543210", "5555555555", "1112223333", "", "5556667777"],
    "account_user": ["qqqqqq", "janesmith", "alicebrown", "bobwhite", "invaliduser", "noaddress"],
    "password_user": ["password123", "password456", "password789", "password101", "", "password111"],
    "confirm_password": ["password123", "password456", "password789", "password101", "", "password111"],
    "result": ["", "", "", "", "", ""]
}


# Tạo DataFrame
df = pd.DataFrame(data)

# Lưu DataFrame vào file Excel
df.to_excel('register_tests.xlsx', index=False)

print("File Excel đã được tạo thành công!")
