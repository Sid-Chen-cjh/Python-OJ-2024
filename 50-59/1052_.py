"""
n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in range(n):
    for j in range(i+1, n):
        if a[i] > a[j]:
            ans += 1
print(ans)

"""


def count_inversions(arr):
    def merge_and_count_split_inv(left, right):
        merged = []
        inversions = 0
        i, j = 0, 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
                inversions += len(left) - i  # All remaining elements in left are inversions with right[j]

        # Append any remaining elements of left and right
        merged.extend(left[i:])
        merged.extend(right[j:])

        return merged, inversions

    def sort_and_count(arr):
        if len(arr) <= 1:
            return arr, 0

        mid = len(arr) // 2
        left, x = sort_and_count(arr[:mid])
        right, y = sort_and_count(arr[mid:])
        merged, z = merge_and_count_split_inv(left, right)

        return merged, x + y + z

    _, num_inversions = sort_and_count(arr)
    return num_inversions


n = int(input())

a = list(map(int, input().split()))
print(count_inversions(a))  # 输出逆序对的数量

