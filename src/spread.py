def range(*arr):
    if type(arr) == list or type(arr) == tuple:
        arr = arr[0]

    arr = sorted(arr)
    return arr[-1] - arr[0]

def inter_quartile_range(*arr):
    if type(arr) == list or type(arr) == tuple:
        arr = arr[0]

    length = len(arr)
    arr = sorted(arr)
    if length % 2 != 0:
        Q2 = arr[length // 2]
        lower = arr[0:length//2]
        length_lower = len(lower)
        Q1 = 0.5 * (lower[length_lower//2 - 1] + lower[length_lower // 2])
        upper = arr[length//2 + 1:length+1]
        length_upper = len(upper)
        Q3 = 0.5 * (upper[length_upper//2 - 1] + upper[length_upper // 2])
        return Q3 - Q1
    else:
        Q2 = 0.5 * (arr[length // 2 - 1] + arr[length // 2])
        lower = arr[0:length//2]
        upper = arr[length//2:length+1]
        length_lower = len(lower)
        length_upper = len(upper)
        Q1 = lower[length_lower // 2]
        Q3 = upper[length_upper // 2]
        return Q3 - Q1

if __name__ == "__main__":
    arr = [11,10,11,11,11,14,8,9,8]
    print(inter_quartile_range(arr))
