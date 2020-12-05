def count_occurences(path, n):
    text = open(path, "r") 
    d = {}
    for line in text: 
        line = line.strip() 
        key, value = line.split(":")
        words = value.split(" ")
        if key in d:
            d[key] += len(words)
        else:
            d[key] = len(words)

    sorted_d = sorted(d.items(), key=lambda item: item[1], reverse=True)
    print(sorted_d[:n])

if __name__ == "__main__":
    x = count_occurences("a.txt", 2)
