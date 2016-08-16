import time
import unittest

from cache import Cacher

cache = Cacher()

@cache
def math(x):
    time.sleep(2)
    return x**2

@cache
def strings(x):
    time.sleep(2)
    return str(x)

@cache
def arguments(x, y=2):
    time.sleep(2)
    return x + y

@cache
def thing():
    time.sleep(2)
    return lambda: "foo"

class TestFoo(unittest.TestCase):
    def test_bar_baz(self):
        self.assertEquals(math(2), 4)
        self.assertEquals(math(2), 4)

    def test_strings(self):
        self.assertEquals(strings(2), "2")
        self.assertEquals(strings(2), "2")

    def test_arguments(self):
        self.assertEquals(arguments(2, y=3), 5)
        self.assertEquals(arguments(2, y=4), 6)

    def test_thing(self):
        self.assertEquals(thing()(), "foo")
        self.assertEquals(thing()(), "foo")


if __name__ == "__main__":
    unittest.main()
