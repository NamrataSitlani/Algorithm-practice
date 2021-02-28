def everyOther(t):
    count = 0
    for i in range(1, len(t)):
        if t[i] == t[i-1]:
            count += 1
    print(count)


if __name__ == "__main__":
    everyOther("xxyxxy")
    everyOther("yyyyy")

