def fibonacci(n):
    fib_sequence = [0, 1]
    if n <= 1:
        return fib_sequence[:n + 1]

    for i in range(2, n + 1):
        next_fib = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_fib)

    return fib_sequence

# 使用示例
n = int(input("請輸入費波納契數列的項數："))
if n < 0:
    print("請輸入一個非負整數。")
else:
    result = fibonacci(n)
    print(f"前 {n} 個費波納契數列項目為：")
    print(result)
