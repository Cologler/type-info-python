# -*- coding: utf-8 -*-
#
# Copyright (c) 2019~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import typing
import collections

from type_info import get_type_info

from utils import generic_as_tuple

def test_chainmap():
    type_info = get_type_info(typing.ChainMap[str, int])
    assert generic_as_tuple(type_info) == (typing.ChainMap, (str, int), collections.ChainMap)
    assert type_info.std_type is collections.ChainMap

def test_counter():
    type_info = get_type_info(typing.Counter[str])
    assert generic_as_tuple(type_info) == (typing.Counter, (str, ), collections.Counter)
    assert type_info.std_type is collections.Counter

def test_defaultdict():
    type_info = get_type_info(typing.DefaultDict[str, int])
    assert generic_as_tuple(type_info) == (typing.DefaultDict, (str, int), collections.defaultdict)
    assert type_info.std_type is collections.defaultdict

def test_deque():
    type_info = get_type_info(typing.Deque[str])
    assert generic_as_tuple(type_info) == (typing.Deque, (str, ), collections.deque)
    assert type_info.std_type is collections.deque

def test_ordereddict():
    type_info = get_type_info(typing.OrderedDict[str, int])
    assert generic_as_tuple(type_info) == (typing.OrderedDict, (str, int), collections.OrderedDict)
    assert type_info.std_type is collections.OrderedDict

