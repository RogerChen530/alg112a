def solve_quadratic_newton(a, b, c, initial_guess, tolerance=1e-6, max_iterations=100):
    x_n = initial_guess

    for iteration in range(max_iterations):
        f_x_n = a*x_n**2 + b*x_n + c
        f_prime_x_n = 2*a*x_n + b

        x_n_minus_1 = x_n - f_x_n / f_prime_x_n

        # 檢查是否收斂
        if abs(x_n_minus_1 - x_n) < tolerance:
            return x_n_minus_1

        x_n = x_n_minus_1

    # 若在迭代次數內未收斂，返回最後的近似解
    return x_n

# 測試方程式 x^2 - 3x + 1 = 0
a = 1
b = -3
c = 1

initial_guess = 0  # 初始猜測值
root = solve_quadratic_newton(a, b, c, initial_guess)
print("Root:", root)
