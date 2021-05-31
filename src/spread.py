from central_tendancy import mean

def range_of_array(*arr):
    if type(arr[0]) == list or type(arr[0]) == tuple:
        arr = arr[0]

    arr = sorted(arr)
    return arr[-1] - arr[0]

def inter_quartile_range(*arr):
    if type(arr[0]) == list or type(arr[0]) == tuple:
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

def mean_absolute_deviation(*arr):
    if type(arr[0]) == list or type(arr[0]) == tuple:
        arr = arr[0]

    length = len(arr)
    mean_arr = mean(arr)
    sum_of_diffs = 0
    for i in range(length):
        sum_of_diffs += arr[i] - mean_arr
    return sum_of_diffs / length

def variance(*arr):
    if type(arr[0]) == list or type(arr[0]) == tuple:
        arr = arr[0]

    length = len(arr)
    mean_arr = mean(arr)
    sum_of_squared_diffs = 0
    for i in range(length):
        sum_of_squared_diffs += (arr[i] - mean_arr) ** 2
    return sum_of_squared_diffs / (length-1)

def standard_deviation(*arr):
    if type(arr[0]) == list or type(arr[0]) == tuple:
        arr = arr[0]

    var = variance(arr)
    from math import sqrt
    return sqrt(var)

if __name__ == "__main__":
    arr = [11,10,11,11,11,14,8,9,8]
    print(inter_quartile_range(arr))
    print(variance(arr))
    print(standard_deviation(arr))
