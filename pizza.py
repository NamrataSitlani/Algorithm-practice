def pizza(arr,slices):
    return (sum([a["num"] for a in arr]) / slices)

if __name__ == '__main__':
    arr = [{"name": "Joe", "num": 9 }, { "name": "Cami", "num": 3 }, { "name": "Cassidy", "num": 4 }]
    print(pizza(arr, 2))
