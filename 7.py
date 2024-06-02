def calculate_divided_differences(x, f):
    n = len(x)
    # Khởi tạo một danh sách 2D cho các sai phân chia
    F = [[0.0 for _ in range(n)] for _ in range(n)]

    # Đặt các giá trị ban đầu cho các sai phân chia
    for i in range(n):
        F[i][0] = f[i]

    # Tính toán các sai phân chia
    for i in range(1, n):
        for j in range(1, i + 1):
            F[i][j] = round((F[i][j - 1] - F[i - 1][j - 1]) / (x[i] - x[i - j]),10)

    return F

def construct_newton_polynomial(F, x):
    n = len(x)
    he_so = [F[i][i] for i in range(n)]
    polynomial = f"{he_so[0]}"
    
    for i in range(1, n):
        term = f"{he_so[i]}"
        for j in range(i):
            term += f"*(x - {x[j]})"
        polynomial += f" + {term}"
    
    return polynomial

# Các điểm đã cho
x = [-0.1, 0.0, 0.2, 0.3]
f = [5.3, 2.0, 3.19, 1.0]

# Tính toán các sai phân chia
F = calculate_divided_differences(x, f)

# Xuất kết quả
print("Các sai phân chia là:")
for i in range(len(F)):
    print(f"F[{i}][{i}] = {F[i][i]}")

# Xây dựng đa thức nội suy
Da_thuc = construct_newton_polynomial(F, x)
print("\nĐa thức nội suy bậc ba là:")
print(Da_thuc)


# Thêm điểm mới
x.append(0.35)
f.append(0.97260)

# Tính các sai phân chia cho tập điểm mới
F = calculate_divided_differences(x, f)

# Xuất kết quả
print("\nCác sai phân chia cho tập điểm mới là:")
for i in range(len(F)):
    print(f"F[{i}][{i}] = {F[i][i]}")

# Xây dựng đa thức nội suy mới
Da_thuc = construct_newton_polynomial(F, x)
print("\nĐa thức nội suy bậc bốn là:")
print(Da_thuc)
