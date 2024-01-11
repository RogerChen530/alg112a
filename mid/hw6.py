import numpy as np

# 函數 f 對變數 p[k] 的偏微分: df / dp[k]
def df(f, p, k, step=1e-5):
    p1 = p.copy()
    p1[k] = p[k] + step
    return (f(p1) - f(p)) / step

# 梯度：函數 f 在點 p 上的梯度
def grad(f, p):
    gp = p.copy()
    for k in range(len(p)):
        gp[k] = df(f, p, k)
    return np.array(gp)

# 梯度下降法
def gradient_descent(f, initial_point, learning_rate=0.01, max_iterations=1000, tolerance=1e-6):
    current_point = np.array(initial_point)

    for iteration in range(max_iterations):
        gradient = grad(f, current_point)
        current_point -= learning_rate * gradient

        # 檢查收斂條件
        if np.linalg.norm(gradient) < tolerance:
            break

    return current_point

# 測試梯度下降法
def objective_function(x):
    return x[0]**2 + x[1]**2 + x[2]**2

initial_point = [1.0, 2.0, 3.0]
learning_rate = 0.1
max_iterations = 1000

result = gradient_descent(objective_function, initial_point, learning_rate, max_iterations)
print("Optimal Point:", result)
print("Optimal Value:", objective_function(result))
