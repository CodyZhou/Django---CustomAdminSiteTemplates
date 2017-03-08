#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 3/8/2017 11:13 AM
# @Author  : Cody Zhou
# @File    : choices.py
# @Software: PyCharm
# Description:
#   Used to define the all choices of this project.
#

# Options for enable and disable
ENABLE_DISABLE_CHOICE = (
    (0, 'Disable'),
    (1, 'Enable')
)

# Options for author's status
AUTHOR_STATUS_CHOICE = (
    (0, 'New Author'),
    (10, 'Author'),
    (20, 'Retirement')
)

# Book Statuses
BOOK_STATUS_CHOICE = (
    (0, 'Arrived'),
    (10, 'New Book For Sale'),
    (15, 'For Sale'),
    (20, 'Discount'),
    (30, 'Discontinued'),
    (40, 'Special Offer'),
    (50, 'Sold Out')
)
