def numChars(string, word):
    count = 0
    for i in list(string):
        if word in i:
            count+= 1
    print(count)

numChars("oh heavens", "h")
