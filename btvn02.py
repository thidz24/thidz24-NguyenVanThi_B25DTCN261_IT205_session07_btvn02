transaction = " nguyEN vAn a | PYTHON-01 | 15000000 | paid "

transaction.strip()

parts = transaction.split("-")

student_name = parts[0].title()
course_code = parts[1]
amount = parts[2]
status = parts[3].upper()

print("Học viên:", student_name)
print("Khóa học:", course_code)
print("Số tiền:", amount,"VND")
print("Trạng thái:", status)

# transaction.strip() không làm thay đổi trực tiếp chuỗi ban đầu vì không được gán lại
# Chuỗi giao dịch thực tế được phân tách bằng ký tự "|"
# transaction.split("-") là sai vì ta thấy chuỗi được phân tách bởi dấu "|"
# Sau khi tách bằng sai delimiter, dữ liệu trong parts bị lệch chỉ tách "PYTHON-01"
# .strip() lại từng phần sau khi split() vì sau khi tách vẫn còn khoảng trắng nên cần .strip() 
# chuyển amount từ chuỗi sang số trước khi định dạng tiền vì amount vẫn là chuỗi, không định dạng được tiền tệ
# Sửa code
transaction = " nguyEN vAn a | PYTHON-01 | 15000000 | paid "
transaction = transaction.strip()

parts = transaction.split("|")

student_name = parts[0].strip().title()
course_code = parts[1].strip()
amount = int(parts[2].strip())
status = parts[3].strip().upper()

print("Học viên:", student_name)
print("Khóa học:", course_code)
print("Số tiền:", amount,"VND")
print("Trạng thái:", status)
