import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price']+quote['top_ask']['price'])/2 ))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price']+quote['top_ask']['price'])/2 ))

  """ ------------ Add more unit tests ------------ """
  def test_getRatio_calculateRatio(self):
    price_a = [0, 126.05, 100, 119.2, 120.48]
    price_b = [150, 120, 100, 108.2, 121.56]
    """ ------------ Add the assertion below ------------ """
    for i in range(0,len(price_a)):
      self.assertEqual(getRatio(price_a[i],price_b[i]), price_a[i]/price_b[i])

  def test_getRatio_ZeroDivision(self):
    price_a = [0, 126.05, 0]
    price_b = [0, 0, 100]
    """ ------------ Add the assertion below ------------ """
    for i in range(0,len(price_a)):
      try:
        self.assertEqual(getRatio(price_a[i],price_b[i]), price_a[i]/price_b[i])
      except ZeroDivisionError as error:
        return "Zero Division Error"

if __name__ == '__main__':
    unittest.main()
