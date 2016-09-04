def list_sum(arr):
    """
    :param arr:
    :return: Given a list [1, 1], increment its value by 1 so it becomes [1, 2]
             In case of [9, 9] as an input, output should be [1, 0, 0]
    """
    i = len(arr) - 1
    return _rec_list_sum(arr, i)

def _rec_list_sum(arr, i):
    if i == 0 and arr[i] == 9:
        arr[i] = 1
        arr.insert(1, 0)
        return arr
    elif i == 0 and arr[i] < 9:
        arr[i] += 1
        return arr
    elif i > 0 and arr[i] < 9:
        arr[i] += 1
        return arr
    elif i > 0 and arr[i] == 9:
        arr[i] = 0
        return _rec_list_sum(arr, i - 1)


arr = [9, 9]
res = list_sum(arr)
print res