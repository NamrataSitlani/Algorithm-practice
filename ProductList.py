class ProductList:
    def __init__(self):
        self.L = []
        self.result = 1
    def add(self, n):
        self.L.append(n)
        return self.L
    def product(self, m):
        x = self.L[-m:]
        for item in x:
            self.result = self.result * item
        return self.result


if __name__=="__main__":
    P = ProductList()
    print(P.add(7))
    print(P.add(0))
    print(P.add(2))
    print(P.add(5))
    print(P.add(4))
    print(P.product(3))

