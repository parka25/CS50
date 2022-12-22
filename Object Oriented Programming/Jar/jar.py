class Jar:
    # initialize a cookie jar with the given capacity.
    # If capacity is a non negative integer, then raise
    # ValueError
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity needs to be a non-negative integer")
        self._capacity = capacity
        self._size = 0
    # return a string with n number of cookies

    def __str__(self):
        return self.size * '🍪'

    # add n cookies to the cookie jar. If this exceeds
    # the capacity, then raise ValueError
    def deposit(self, n):
        if n > self.capacity:
            raise ValueError("Exceeds Capacity")
        if n + self.size > self.capacity:
            raise ValueError("Exceeds Capacity")
        self._size += n
    # remove n cookies from the cookie jar. If aren't
    # that many cookies in the cookie jar, raise Value
    # Error

    def withdraw(self, n):
        if self.size < n:
            raise ValueError("Not Enough Cookies")
        self._size -= n
    # return cookie jar's capacity

    @property
    def capacity(self):
        return self._capacity
    # return the number of cookies in the cookie jar

    @property
    def size(self):
        return self._size
