import numpy as np
from scipy import optimize

def solve_polynomial(coefficients):
    # 將多項式的係數轉換為numpy陣列
    coefficients = np.array(coefficients)

    # 使用SciPy的roots函數找到多項式的根
    roots = np.roots(coefficients)

    return roots

# 測試解 n 次多項式，例如 x^2 - 4 = 0
coefficients = [1, 0, -4]  # 對應 x^2 - 4
roots = solve_polynomial(coefficients)

print("Polynomial Coefficients:", coefficients)
print("Roots:", roots)
