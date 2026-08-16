class StockSpanner:

    def __init__(self):
        self.arr = []

    def next(self, price: int) -> int:
        self.arr.append(price)
        n = len(self.arr)-2
        while n >= 0 and self.arr[n] <= price:
            n -= 1
            
        return len(self.arr) - n - 1

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)