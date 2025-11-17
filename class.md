# 🧑‍🏫 **BÀI TẬP: Quản lý thú cưng — Hiểu BẢN CHẤT của Class & Object**

## 🎯 **Mục tiêu**

Giúp bạn hiểu thật rõ:

* **Class = bản thiết kế**
* **Object = sản phẩm được tạo ra từ bản thiết kế**
* Mỗi object có **dữ liệu riêng**, **trạng thái riêng**, và **không ảnh hưởng nhau**
* Khi cần quản lý nhiều thực thể giống nhau → class là công cụ phù hợp nhất

---

# 📘 **YÊU CẦU BÀI TẬP**

## **1. Tạo một class `Pet`**

Class này mô tả **một thú cưng**.

Thuộc tính mỗi thú cưng có:

* `name` – tên thú cưng
* `species` – loài (dog, cat…)
* `hunger` – độ đói (0–100, càng lớn càng đói)

Phương thức:

* `feed(amount)`
  → giảm chỉ số `hunger` đi `amount`, thấp nhất là 0
* `status()`
  → trả về chuỗi `"Name: ..., Species: ..., Hunger: ..."`

---

## **2. Tạo NHIỀU đối tượng từ class `Pet`**

Ví dụ trong `main.py`:

* Tạo 3 thú cưng: chó, mèo, thỏ
* Cho từng con ăn khác nhau
* In trạng thái từng con

---

## **3. Chứng minh tính độc lập của từng object**

Viết code chứng minh:

* Khi bạn cho **con chó** ăn,
  → **con mèo không no lên theo**
* Khi chỉnh `hunger` của **con mèo**,
  → **con thỏ không bị ảnh hưởng**

(*Đây chính là mục tiêu quan trọng nhất*)

---

# 🧪 **Gợi ý kiểm tra**

Sau khi cho con chó ăn, in:

```python
print(dog.status())
print(cat.status())
print(rabbit.status())
```

Kết quả mục tiêu:

* Mỗi object là **một vùng dữ liệu độc lập**
* Class chỉ là **khuôn mẫu**, không giữ trạng thái
* Objects mới là nơi **lưu trữ dữ liệu thật**

---

# 📝 **Gợi ý output mẫu kỳ vọng**

Ví dụ:

```
Before feeding:
Dog hunger: 80
Cat hunger: 50
Rabbit hunger: 30

After feeding dog 40:
Dog hunger: 40
Cat hunger: 50
Rabbit hunger: 30
```



### **Tại sao phải dùng class?**
Trả lời câu hỏi