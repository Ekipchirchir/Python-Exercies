class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer.")
        self.capacity = capacity
        self.cookies = 0

    def __str__(self):
        return "🍪" * self.cookies

    def deposit(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("The number of cookies to deposit must be a non-negative integer.")
        if self.cookies + n > self.capacity:
            raise ValueError("The jar does not have enough capacity to store all the cookies.")
        self.cookies += n

    def withdraw(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("The number of cookies to withdraw must be a non-negative integer.")
        if self.cookies < n:
            raise ValueError("The jar does not have enough cookies to withdraw.")
        self.cookies -= n

    @property
    def size(self):
        return self.cookies
