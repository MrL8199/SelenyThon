
# 🧪 **BÀI TẬP OOP: Hệ thống quản lý Test Case đơn giản**

---

# 🎯 **MỤC TIÊU BÀI TẬP**

Sau khi làm xong, học viên phải hiểu được:

* **Class dùng để mô tả một loại đối tượng** (ở đây là TestCase và TestSuite)
* **Mỗi object là một test case độc lập**
* TestSuite chỉ là nơi **quản lý danh sách** các TestCase
* Thay đổi trạng thái của test case A **không ảnh hưởng** test case B
* Biết cách viết method để thay đổi trạng thái của từng object

---

# 📘 **PHẦN 1 — YÊU CẦU TẠO CLASS `TestCase`**

Class này mô tả **một test case duy nhất**.

## 🎛 **Thuộc tính (Attributes)**

### 1. `id` (string hoặc int)

* Mã test case.
* Ví dụ: `"TC001"`, `"TC002"`.

### 2. `title` (string)

* Tên hoặc mô tả ngắn gọn của test case.
* Ví dụ: `"Login with valid credentials"`.

### 3. `expected_result` (string)

* Giá trị mong đợi khi chạy test.
* Ví dụ: `"Success"`, `"Error message displayed"`.

### 4. `status` (string)

* Trạng thái hiện tại của test case.
* Giá trị hợp lệ:

  * `"Not Run"`  *(default)*
  * `"Passed"`
  * `"Failed"`

---

# 🔧 **PHẦN 2 — YÊU CẦU CHI TIẾT CÁC METHOD CỦA `TestCase`**

---

## **1. Method `run(self, actual_result)`**

### Chức năng:

* Chạy test case bằng cách so sánh `actual_result` với `expected_result`.

### Tham số:

* `actual_result` (string): kết quả thực tế khi chạy test.

### Yêu cầu xử lý:

1. Nếu `actual_result == expected_result`
   → đặt `status = "Passed"`
2. Ngược lại
   → đặt `status = "Failed"`

### Không cần return gì.

---

## **2. Method `reset(self)`**

### Chức năng:

* Đưa test case về trạng thái chưa chạy.

### Yêu cầu xử lý:

```
status = "Not Run"
```

---

## **3. Method `info(self)`**

### Chức năng:

* Trả về thông tin chi tiết của test case dưới dạng string.

### Output format:

```
[TC<ID>] <title> - Status: <status>
Expected: <expected_result>
```

Ví dụ:

```
[TC001] Login valid - Status: Passed
Expected: Success
```

---

# 📘 **PHẦN 3 — TẠO CLASS `TestSuite`**

Class này quản lý danh sách nhiều test case.

## 🎛 **Thuộc tính**

### 1. `cases` (list)

* Danh sách chứa các object `TestCase`.

---

# 🔧 **PHẦN 4 — YÊU CẦU CHI TIẾT CÁC METHOD CỦA `TestSuite`**

---

## **1. Method `add_case(self, test_case)`**

### Chức năng:

* Thêm một TestCase vào danh sách.

### Tham số:

* `test_case`: object kiểu `TestCase`.

### Yêu cầu xử lý:

* Append vào `self.cases`.

---

## **2. Method `run_all(self)`**

### Chức năng:

* Chạy toàn bộ test case trong suite.

### Yêu cầu xử lý:

* Với mỗi `tc` trong `self.cases`, gọi:

  ```
  tc.run(tc.expected_result)
  ```

  (giả lập luôn đúng)

---

## **3. Method `get_summary(self)`**

### Chức năng:

* Tính tổng số test case theo từng trạng thái.

### Output:

Trả về dictionary:

```
{
  "Passed": x,
  "Failed": y,
  "Not Run": z
}
```

### Yêu cầu xử lý:

* Duyệt tất cả `self.cases`
* Đếm số lượng theo `tc.status`

---

## **4. Method `list_cases(self)`**

### Chức năng:

* In info của tất cả test case.

### Yêu cầu xử lý:

* Với mỗi test case, gọi `tc.info()` và print ra.

---

# 📘 **PHẦN 5 — TẠO FILE `main.py` ĐỂ THỬ NGHIỆM**

Trong `main.py`, làm đầy đủ các bước sau:

---

## **1. Tạo 3 test cases:**

```python
tc1 = TestCase("TC001", "Login với đúng thông tin", "Success")
tc2 = TestCase("TC002", "Login với sai mật khẩu", "Error")
tc3 = TestCase("TC003", "Check nút Login hiển thị", "Visible")
```

---

## **2. Tạo `TestSuite` và thêm các test case vào**

```python
suite = TestSuite()
suite.add_case(tc1)
suite.add_case(tc2)
suite.add_case(tc3)
```

---

## **3. Chạy từng test case với actual_result tùy ý**

Ví dụ:

```python
tc1.run("Success")
tc2.run("Error")
tc3.run("Not Visible")
```

---

## **4. In trạng thái từng test case**

```python
print(tc1.info())
print(tc2.info())
print(tc3.info())
```

---

## **5. In summary**

```python
print(suite.get_summary())
```

---

# 🎯 **PHẦN 6 — MỤC TIÊU HỌC SINH PHẢI RÚT RA**

1. **Mỗi test case là một object độc lập**

   * Thay đổi `tc1.status` không ảnh hưởng `tc2`.

2. **TestSuite không chứa trạng thái của test case**

   * Nó chỉ *quản lý danh sách*.

3. **Class cho phép mô tả thực thể có chung cấu trúc nhưng dữ liệu khác nhau**.

4. **Khi mở rộng (thêm priority, steps, tags…) chỉ cần chỉnh class, không cần viết lại từng case**.

---

