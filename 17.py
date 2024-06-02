def calculate_missing_entries():
    x = [0.0, 0.4, 0.7]
    
    # Định nghĩa các sai phân chia đã biết
    f = [None, None, 6]
    f_x1_x2 = 10
    f_x0_x1_x2 = 50 / 7

    # Tính f[x1] sử dụng f[x1, x2]
    f[1] = 6 - f_x1_x2 * (x[2] - x[1])

    # Tính f[x0] sử dụng f[x0, x1, x2]
    f_x0_x1 = f_x1_x2 - f_x0_x1_x2 * (x[2] - x[0])
    f[0] = f[1] - (f_x1_x2 - f_x0_x1_x2 * (x[2] - x[0])) * (x[1] - x[0])

    print("Các giá trị đã tính toán:")
    print(f"f[x0] = {round(f[0],10)}")
    print(f"f[x1] = {round(f[1],10)}")
    print(f"f[x2] = {f[2]}")
    print(f"f[x0, x1] = {f_x0_x1}")
    print(f"f[x1, x2] = {f_x1_x2}")
    print(f"f[x0, x1, x2] = {round(f_x0_x1_x2,10)}")

calculate_missing_entries()
