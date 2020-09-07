def stockBuySell(stock_list):
    buy = stock_list.index(min(stock_list)) +1
    sell = stock_list.index(max(stock_list)) +1
    return f'buy on day {buy}, sell on day {sell}'
if __name__ == '__main__':
    stock_list = [110, 180, 260, 40, 310, 535, 695]
    print(stockBuySell(stock_list))
