import numpy as np
from micrograd import Tensor

# 函數 f 對變數 p[k] 的偏微分: df / dp[k]
def df(f, p, k):
    p = [Tensor(v) for v in p]
    f_val = f(p)
    f_val.backward()
    return p[k].grad.data

# 梯度：函數 f 在點 p 上的梯度
def grad(f, p):
    p = [Tensor(v) for v in p]
    f_val = f(p)
    f_val.backward()
    return [v.grad.data for v in p]

# 梯度下降法
def gradient_descent(f, initial_point, learning_rate=0.01, max_iterations=1000, tolerance=1e-6):
    current_point = [Tensor(v) for v in initial_point]

    for iteration in range(max_iterations):
        gradient = grad(f, current_point)
        current_point = [v - learning_rate * g for v, g in zip(current_point, gradient)]

        # 檢查收斂條件
        if np.linalg.norm([g.data for g in gradient]) < tolerance:
            break

    return [v.data for v in current_point]

# 測試梯度下降法
def objective_function(x):
    # 這是一個簡單的例子，你需要根據你的實際問題定義目標函數
    return sum(v**2 for v in x)

initial_point = [1.0, 2.0, 3.0]
learning_rate = 0.1
max_iterations = 1000

result = gradient_descent(objective_function, initial_point, learning_rate, max_iterations)
print("Optimal Point:", result)
print("Optimal Value:", objective_function(result))
