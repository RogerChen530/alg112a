import cmath

def solve_quadratic_bruteforce(a, b, c):
    # 計算判別式
    delta = b**2 - 4*a*c
    
    # 計算兩個解
    root1 = (-b + cmath.sqrt(delta)) / (2*a)
    root2 = (-b - cmath.sqrt(delta)) / (2*a)

    return root1, root2

# 測試方程式 x^2 - 3x + 1 = 0
a = 1
b = -3
c = 1

roots = solve_quadratic_bruteforce(a, b, c)
print("Root 1:", roots[0])
print("Root 2:", roots[1])
