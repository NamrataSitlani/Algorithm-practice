def stringMultiply(x,y):
    res = 0
    carry1 = 1
    carry2 = 1


    for i in x[::-1]:
        carry2 = 1
        for j in y[::-1]:
            res += int(i)*int(j)* carry1 * carry2
            carry2 *= 10
        carry1 *= 10
    return str(res)

if __name__ == "__main__":
    s1 = stringMultiply("123", "456")
    print(s1)
