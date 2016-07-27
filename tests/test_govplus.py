# -*- coding: utf-8 -*-
from nose.tools import assert_equal
from domplus import govplus


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
