def min_value(arr):
    #Assigning the first value of the list as minimum value
    min_value = arr[0]
    for i in range(len(arr)):
        if arr[i]< min_value:
            #Set the new minimum value if the other value in the list is smaller than min_value
            min_value= arr[i]
            return min_value

if __name__ == '__main__':
    arr = [7,9,0,2,4]
    print(min_value(arr))
