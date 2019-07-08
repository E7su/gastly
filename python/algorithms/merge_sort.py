def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def merge_sort(list):
    if len(list) < 2:
        return list
    middle = len(list) / 2
    left = merge_sort(list[:middle])
    right = merge_sort(list[middle:])
    return merge(left, right)


if __name__ == "__main__":
    a = [4, 235, 2, 0]
    res = merge_sort(a)
    print(res)
