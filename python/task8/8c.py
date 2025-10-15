def merge_descending(list1, list2):
    i, j = 0, 0
    merged = []

    while i < len(list1) and j < len(list2):
        if list1[i] >= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1

    while i < len(list1):
        merged.append(list1[i])
        i += 1

    while j < len(list2):
        merged.append(list2[j])
        j += 1

    return merged

# ---- Driver Code ----
t = int(input())   # number of test cases
for _ in range(t):
    n, m = map(int, input().split())
    list1 = list(map(int, input().split()))
    list2 = list(map(int, input().split()))

    result = merge_descending(list1, list2)
    print(*result)
