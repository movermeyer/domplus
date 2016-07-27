#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_domplus
----------------------------------

Tests for `domplus` module.
"""


import unittest
from domplus import govplus


class TestDomplus(unittest.TestCase):

    def setUp(self):
        self.cpfs_valid = ['03167158590', '467.368.255-63', '467368255-63']
        self.cpfs_invalid = ['46736825566', '03167158590A', '467.368.255/63', '467368255638', '4673682556']

    def test_valid_br_cpf_type_int(self):
        self.assertTrue(govplus.is_valid_br_cpf(46736825563), "Valid cpf type int how success!")

    def test_valid_br_cpf(self):
        self.assertTrue(all(govplus.is_valid_br_cpf(cpf) for cpf in self.cpfs_valid), "All Cpfs Valid how success!")

    def test_invalid_br_cpf(self):
        self.assertTrue(all(True if govplus.is_valid_br_cpf(cpf) is False else False for cpf in self.cpfs_invalid), "Cpfs Invalids")

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
