def arrayDiff(arr,value):
    count = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] - arr[i] == value or arr[i] - arr[j] == value:
                count = count+1
    return count

if __name__ == '__main__':
    print(arrayDiff([1,2,3,4], 1))
