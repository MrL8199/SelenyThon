

# 🔋 **BÀI TẬP CHI TIẾT: Quản lý Pin của Thiết Bị (Battery Simulation)**

## 🎯 Mục tiêu của bài tập

* Hiểu rõ **class** dùng để mô tả một nhóm các đối tượng có chung tính chất.
* Biết cách tạo **object** và thấy sự **độc lập** giữa các đối tượng.
* Biết cách viết **method**, nhận tham số, thay đổi trạng thái của object.
* Thấy rõ việc mô phỏng trạng thái thiết bị (pin, bật/tắt) bằng OOP.

---

# 📘 **PHẦN 1 — YÊU CẦU TẠO CLASS `Device`**

Tạo một *class* tên **`Device`** mô phỏng một thiết bị điện tử. (device.py)

## 🎛 **Thuộc tính (Attributes)**

Mỗi đối tượng `Device` cần có các thuộc tính sau:

### 1. `name` (string)

* Tên thiết bị
* Ví dụ: `"Phone"`, `"Tablet"`, `"Smartwatch"`

### 2. `battery` (integer 0–100)

* Mức pin hiện tại của thiết bị (tính bằng %)
* Chỉ số này sẽ thay đổi khi dùng pin hoặc sạc pin

### 3. `status` (string)

* Chỉ nhận 1 trong 2 giá trị:

  * `"on"`
  * `"off"`
* Giá trị mặc định: `"off"`

---

# 🔧 **PHẦN 2 — YÊU CẦU CÁC METHOD TRONG CLASS `Device`**

Dưới đây là yêu cầu cực kỳ chi tiết cho từng method:

---

## **1. Method `turn_on(self)`**

### Chức năng:

* Bật thiết bị

### Yêu cầu xử lý:

* Nếu pin (`battery`) = 0 → **không thể bật**, giữ nguyên trạng thái `"off"`
* Nếu pin > 0 → đặt `status = "on"`

### Không cần return gì.

---

## **2. Method `turn_off(self)`**

### Chức năng:

* Tắt thiết bị

### Yêu cầu xử lý:

* Đơn giản đặt `status = "off"`

### Không cần return gì.

---

## **3. Method `use(self, amount)`**

### Chức năng:

* Giảm pin thiết bị khi sử dụng

### Tham số:

* `amount` (int): số phần trăm pin bị tiêu hao

### Yêu cầu xử lý:

1. Chỉ cho phép sử dụng khi trạng thái là `"on"`

   * Nếu đang `"off"` → không trừ pin
2. Giảm pin:

   ```
   battery = battery - amount
   ```
3. Nếu sau khi trừ pin mà `< 0` → đặt pin = 0
4. Nếu pin trở thành 0 → tự động chuyển trạng thái về `"off"`

### Không cần return.

---

## **4. Method `charge(self, amount)`**

### Chức năng:

* Sạc pin cho thiết bị

### Tham số:

* `amount` (int): số phần trăm pin được nạp thêm

### Yêu cầu xử lý:

1. Tăng pin:

   ```
   battery = battery + amount
   ```
2. Nếu vượt quá 100 → đặt pin = 100
3. Không thay đổi trạng thái (thiết bị đang on hay off vẫn giữ nguyên)

### Không cần return.

---

## **5. Method `info(self)`**

### Chức năng:

* Trả về thông tin thiết bị dạng string

### Output dạng:

```
Device: <name> | Battery: <battery>% | Status: <status>
```

Ví dụ:

```
Device: Phone | Battery: 45% | Status: on
```

---

# 📘 **PHẦN 3 — YÊU CẦU TẠO NHIỀU OBJECT VÀ THỬ NGHIỆM**

Trong file `main.py`, làm các bước sau:

## 1. Tạo 3 thiết bị:

```python
phone = Device("Phone", 100)
tablet = Device("Tablet", 30)
watch = Device("Smartwatch", 10)
```

## 2. Thực hiện các hành động:

* Bật cả 3 thiết bị
* Dùng pin:

  * Phone dùng 60%
  * Tablet dùng 10%
  * Watch dùng 15%
* Sạc:

  * Sạc Watch thêm 50%

## 3. In thông tin từng thiết bị:

```python
print(phone.info())
print(tablet.info())
print(watch.info())
```

---

# 🧪 **PHẦN 4 — MỤC TIÊU HIỂU ĐƯỢC QUA KẾT QUẢ**

Học viên phải thấy rõ:

### ✔ Khi dùng pin của **phone**, pin của **tablet** và **watch** không đổi

→ **Mỗi object chứa dữ liệu riêng**

### ✔ Khi watch tụt pin về 0 → tự tắt

→ **Hành vi phụ thuộc trạng thái riêng của từng object**

### ✔ Khi sạc watch → chỉ watch tăng pin

→ Objects **không ảnh hưởng nhau**

---

### Yêu cầu phụ: sử dụng if __name__ == "__main__":