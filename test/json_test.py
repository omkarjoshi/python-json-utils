import unittest

from converter import writer
from core import reader
from main import Order, Item

items = [Item(itemid="Item1", quantity=2, unitprice=2),
             Item(itemid="Item2", quantity=2, unitprice=2)]

order = Order(orderid="ORDER1", items=items)


class MyTestCase(unittest.TestCase):
    def test_converttojson(self):
        try:
            f = reader._readfile("./data/order.json")
            try:
                requireddata = f.readline()
                actualdata = writer.writetostring(order)
                self.assertEqual(requireddata, actualdata)
            finally:
                f.close()
        except IOError:
            raise IOError()

if __name__ == '__main__':
    unittest.main()
