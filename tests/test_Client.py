# -*- coding: utf-8 -*-
import unittest
from pycdek import Client


class TestCDEKClient(unittest.TestCase):
    """
    Тестирование класса Client для работы со СДЭК
    """

    # 1. Данные класса клиента для авторизации
    def test_get_user_info(self):
        client = Client(login='login', password='pswd')
        self.assertEqual(client._login, 'login')
        self.assertEqual(client._password, 'pswd')

    # 2. Выполнение запроса с неопознанным методом
    def test__exec_request(self):
        self.assertRaises(NotImplementedError, Client._exec_request, '', [], 'PUT')

    # 3. Парсинг неокрректного xml
    def test__parse_xml(self):
        parsed_xml = Client._parse_xml('<note><to>Tove</too></note>')
        self.assertIsNone(parsed_xml)
