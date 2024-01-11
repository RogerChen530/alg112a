def min_edit_distance(str1, str2):
    # 如果其中一個字串為空，返回另一個字串的長度
    if len(str1) == 0:
        return len(str2)
    if len(str2) == 0:
        return len(str1)

    # 如果最後一個字符相同，不進行任何編輯操作
    if str1[-1] == str2[-1]:
        return min_edit_distance(str1[:-1], str2[:-1])

    # 否則，考慮三種操作：插入、刪除、替換
    insert_cost = 1 + min_edit_distance(str1, str2[:-1])
    delete_cost = 1 + min_edit_distance(str1[:-1], str2)
    replace_cost = 1 + min_edit_distance(str1[:-1], str2[:-1])

    # 返回三種操作的最小成本
    return min(insert_cost, delete_cost, replace_cost)

# 測試
str1 = "kitten"
str2 = "sitting"
distance = min_edit_distance(str1, str2)
print(f"最小編輯距離 between '{str1}' and '{str2}': {distance}")
