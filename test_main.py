# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 20:12:40 2020

@author: solcanma
"""
import main


def test_reverse_and_upper():
    """Tests if reversing and uppercasing."""
    assert main.reverse_and_upper("Smakyna") == "ANYKAMS"


def test_reverse_and_upper_space():
    """Tests if reversing and uppercasing."""
    assert main.reverse_and_upper("Smakyna aaa") == "AAA ANYKAMS"
