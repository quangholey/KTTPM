const getBookApi = "http://127.0.0.1:5000/book-management/books";
const addBookApi = "http://127.0.0.1:5000/book-management/book";

// Hàm khởi tạo
function start() {
    handleCreateForm(); // Đăng ký hàm xử lý form
}

// Hàm xử lý khi gửi form
function handleCreateForm() {
    var form = document.getElementById('book-form');

    form.onsubmit = function(e) {
        e.preventDefault(); // Ngăn chặn hành động gửi form mặc định

        // Lấy dữ liệu từ các trường trong form
        var name = document.getElementById('bookName').value;
        var pageCount = parseInt(document.getElementById('pageCount').value);
        var author_name = (document.getElementById('authorId').value);
        var categoryId = parseInt(document.getElementById('categoryId').value);

        // Kiểm tra nếu các trường đều có giá trị hợp lệ
        if (name && !isNaN(pageCount) && (author_name) && !isNaN(categoryId)) {
            const data = {
                name: name,
                page_count: pageCount,
                author_name: author_name,
                category_id: categoryId
            };
            createBook(data); // Gửi dữ liệu tới API để thêm sách
        } else {
            alert("Vui lòng điền đầy đủ thông tin hợp lệ"); // Thông báo nếu có trường không hợp lệ
        }
    }
}

// Hàm gửi yêu cầu thêm sách đến API
function createBook(data) {
    const options = {
        method: 'POST',
        body: JSON.stringify(data),
        headers: {
            'Content-Type': 'application/json'
        }
    };
    fetch(addBookApi, options)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log("Sách đã được thêm thành công:", data); // Thông báo thành công
            alert("Thêm sách mới thành công!"); // Thông báo thành công cho người dùng
        })
        .catch(error => {
            console.error('Lỗi khi thêm sách:', error);
            alert("Không thể thêm sách. Vui lòng kiểm tra lại.");
        });
}

// Gọi hàm khởi tạo
start();
