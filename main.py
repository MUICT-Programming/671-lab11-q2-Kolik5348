def summation(lst1, lst2):
    updated_list = [a + b for a, b in zip(lst1, lst2)]
    return updated_list

def find_min_max(updated_list):
    min_value = min(updated_list)
    max_value = max(updated_list)
    return min_value, max_value

n = int(input())
lst1 = [int(input()) for i in range(n)]
lst2 = [int(input()) for i in range(n)]

updated_list = summation(lst1, lst2)
min_value, max_value = find_min_max(updated_list)

print(updated_list)
print((min_value, max_value))
