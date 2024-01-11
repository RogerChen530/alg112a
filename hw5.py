import numpy as np

def hill_climbing(objective_function, initial_solution, step_size, max_iterations):
    current_solution = np.array(initial_solution)
    
    for iteration in range(max_iterations):
        current_value = objective_function(current_solution)
        print(f"Iteration {iteration + 1}: Current Value = {current_value}, Current Solution = {current_solution}")

        # 嘗試在鄰近的點中找到更好的解
        neighbor_solution = current_solution + np.random.uniform(-step_size, step_size, size=len(current_solution))
        neighbor_value = objective_function(neighbor_solution)

        # 如果鄰近的點更好，則移動到該點
        if neighbor_value > current_value:
            current_solution = neighbor_solution

    return current_solution

# 測試爬山演算法
def objective_function(x):
    return -((x[0]-2)**2 + (x[1]-3)**2)

initial_solution = [0, 0]
step_size = 0.1
max_iterations = 100

result = hill_climbing(objective_function, initial_solution, step_size, max_iterations)
print("\nOptimal Solution:", result)
print("Optimal Value:", objective_function(result))
