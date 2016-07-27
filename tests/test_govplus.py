# -*- coding: utf-8 -*-
from nose.tools import assert_equal
from domplus import govplus
import unittest

INVALID_CPF = (
    '00000000000',
    '00000000191',
    '99999999999',
    '11111111111',
    '22222222222',
    '33333333333',
    '44444444444',
    '55555555555',
    '66666666666',
    '77777777777',
    '88888888888',
    '99999999999',
    '46736825566',
    '03167158590A',
    '467.368.255/63',
    '467368255638',
    '4673682556'
)


INVALID_CNPJ = (
    '11111111000191',
    '00000000000000',
    '22222222000191',
    '33333333000191',
    '44444444000191',
    '55555555000191',
    '66666666000191',
    '77777777000191',
    '88888888000191',
    '99999999000191',
)


class TestGovplus(unittest.TestCase):

    def setUp(self):
        self.cpfs_valid = ['03167158590', '467.368.255-63', '467368255-63']
        self.cpfs_invalid = INVALID_CPF

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

def test_is_valid_br_cnpj():
    """
    Test is_valid_br_cnpj
    """
    # True
    assert_equal(True, govplus.is_valid_br_cnpj('11444777000161'))
    assert_equal(True, govplus.is_valid_br_cnpj('11.444.777/0001-61'))

    # False
    for i in range(10):
        text = str(i) * 14
        yield check_br_cnpj_False, text

    # invalid cnpj
    assert_equal(False, govplus.is_valid_br_cnpj('84917968000166'))
    assert_equal(False, govplus.is_valid_br_cnpj('11444777000161A'))
    # if accept not string
    assert_equal(False, govplus.is_valid_br_cnpj(64746812000163))
    # if special character =! . / -
    assert_equal(False, govplus.is_valid_br_cnpj('64.746.812/0001,63'))
    # if lenth > 14
    assert_equal(False, govplus.is_valid_br_cnpj('647468120001631'))
    # if lenth < 14
    assert_equal(False, govplus.is_valid_br_cnpj('6474681200016'))

    for invalid_cnpj in INVALID_CNPJ:
        yield check_br_cnpj_False, invalid_cnpj


def check_br_cnpj_False(cnpj):
    assert_equal(False, govplus.is_valid_br_cnpj(cnpj))


def is_br_cpf_or_cnpj():
    """
    Test is_valid_br_cpf_or_cnpj
    """
    # 'cpf' or 'cnpj'
    assert_equal('cpf', govplus.is_br_cpf_or_cnpj('03167158590'))  # valid cpf
    assert_equal('cnpj', govplus.is_br_cpf_or_cnpj('11444777000161'))  # valid cnpj

    # False
    assert_equal(False, govplus.is_br_cpf_or_cnpj('46736825566'))  # invalid cpf
    assert_equal(False, govplus.is_br_cpf_or_cnpj('84917968000166'))  # invalid cnpj
    assert_equal(False, govplus.is_br_cpf_or_cnpj('0316715859'))  # < 11 digits
    assert_equal(False, govplus.is_br_cpf_or_cnpj('031671585900'))  # == 12 digits
    assert_equal(False, govplus.is_br_cpf_or_cnpj('0316715859001'))  # == 13 digits
    assert_equal(False, govplus.is_br_cpf_or_cnpj('1144477700016'))  # == 13 digits
    assert_equal(False, govplus.is_br_cpf_or_cnpj('114447770001610'))  # > 14 digits
