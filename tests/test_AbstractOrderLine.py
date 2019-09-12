# -*- coding: utf-8 -*-
import unittest
from pycdek import AbstractOrderLine


class MyAbstractOrderLine(AbstractOrderLine):
    """
    Класс-наследник от AbstractOrderLine для тестирования
    его неабстрактных методов.
    Реализует абстрактные методы на уровне заглушек (возвращает None)
    """

    def get_product_upc(self):
        return None

    def get_product_weight(self):
        return None

    def get_product_price(self):
        return None

    def get_product_payment(self):
        return None

    def get_product_title(self):
        return None


class TestCDEKAbstractOrderLine(unittest.TestCase):
    """
    Тестирование класса AbstractOrderLine (через наследника MyAbstractOrderLine)
    """
    def setUp(self):
        self.order_line = MyAbstractOrderLine()

    # 0. Покрываем тестами свою реализацию
    def test_get_product_upc(self):
        self.assertEqual(self.order_line.get_product_upc(), None)

    def test_get_product_weight(self):
        self.assertEqual(self.order_line.get_product_weight(), None)

    def test_get_product_price(self):
        self.assertEqual(self.order_line.get_product_price(), None)

    def test_get_product_payment(self):
        self.assertEqual(self.order_line.get_product_payment(), None)

    def test_get_product_title(self):
        self.assertEqual(self.order_line.get_product_title(), None)

    # 1. Метод get_quantity для не заданного значения
    def test_get_quantity_None(self):
        self.assertRaises(AttributeError, self.order_line.get_quantity)

    # 2. Метод get_quantity для заданного значения
    def test_get_quantity_Value(self):
        self.order_line.quantity = 5
        self.assertEqual(self.order_line.get_quantity(), 5)
