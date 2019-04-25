# -*- coding: utf-8 -*-
#
# Copyright (c) 2019~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import sys
import typing
import collections

import pytest

from type_info import get_type_info

def test_chainmap():
    type_info = get_type_info(typing.ChainMap[str, int])
    assert type_info.is_generic
    assert type_info.generic_type == typing.ChainMap
    assert type_info.generic_args == (str, int)
    assert type_info.dynamic_type == collections.ChainMap
    assert type_info.std_type is collections.ChainMap

def test_counter():
    type_info = get_type_info(typing.Counter[str])
    assert type_info.is_generic
    assert type_info.generic_type == typing.Counter
    assert type_info.generic_args == (str, )
    assert type_info.dynamic_type == collections.Counter
    assert type_info.std_type is collections.Counter

def test_defaultdict():
    type_info = get_type_info(typing.DefaultDict[str, int])
    assert type_info.is_generic
    assert type_info.generic_type == typing.DefaultDict
    assert type_info.generic_args == (str, int)
    assert type_info.dynamic_type == collections.defaultdict
    assert type_info.std_type is collections.defaultdict

def test_deque():
    type_info = get_type_info(typing.Deque[str])
    assert type_info.is_generic
    assert type_info.generic_type == typing.Deque
    assert type_info.generic_args == (str, )
    assert type_info.dynamic_type == collections.deque
    assert type_info.std_type is collections.deque

@pytest.mark.skipif(sys.version_info[:3] < (3, 7, 2), reason='typing.OrderedDict was add on 3.7.2')
def test_ordereddict():
    type_info = get_type_info(typing.OrderedDict[str, int])
    assert type_info.is_generic
    assert type_info.generic_type == typing.OrderedDict
    assert type_info.generic_args == (str, int)
    assert type_info.dynamic_type == collections.OrderedDict
    assert type_info.std_type is collections.OrderedDict

