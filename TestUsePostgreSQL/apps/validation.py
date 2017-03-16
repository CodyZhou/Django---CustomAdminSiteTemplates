#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 3/15/2017 12:58 PM
# @Author  : Cody Zhou
# @File    : validation.py
# @Software: PyCharm
# @Description:
#   Used to do variable validation for all models
#

from django.core.exceptions import ValidationError


def validator_number(value):
    """
        Used to check whether the value is all digital.
    """
    if not value.isdigit():
        raise ValidationError("Please input digital in this field!")

    return value


def validator_special_character(value):
    """
        Used to check whether the value contains special character.
    """
    special_character_list = ['%', '>', '<', '?', '=']

    result = [x for x in special_character_list if x in value]

    if len(result) >= 1:
        raise ValidationError("Please do not input special characters in this field!")

    return value

