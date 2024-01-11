from itertools import permutations

def generate_permutations(elements):
    # 使用permutations函數生成所有可能的排列
    all_permutations = permutations(elements)

    # 將結果轉換為列表並返回
    return list(all_permutations)

# 測試程式碼
elements = [1, 2, 3]
result = generate_permutations(elements)

for perm in result:
    print(perm)
