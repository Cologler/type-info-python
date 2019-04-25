# -*- coding: utf-8 -*-
#
# Copyright (c) 2019~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import typing
import collections

from type_info import get_type_info

from utils import generic_as_tuple, typevar_as_tuple, ANY

def test_dict():
    type_info = get_type_info(typing.Dict[str, int])
    assert generic_as_tuple(type_info) == (typing.Dict, (str, int), dict)
    assert type_info.std_type is dict

def test_frozenset():
    type_info = get_type_info(typing.FrozenSet[str])
    assert generic_as_tuple(type_info) == (typing.FrozenSet, (str, ), frozenset)
    assert type_info.std_type is frozenset

def test_list_opened():
    type_info = get_type_info(typing.List)
    assert generic_as_tuple(type_info) == (typing.List, ANY, list)
    assert type_info.std_type is list
    value_type_info = generic_as_tuple(type_info)[1][0]
    assert typevar_as_tuple(value_type_info) == ((), False, False)

def test_list():
    type_info = get_type_info(typing.List[str])
    assert generic_as_tuple(type_info) == (typing.List, (str, ), list)
    assert type_info.std_type is list

def test_set():
    type_info = get_type_info(typing.Set[str])
    assert generic_as_tuple(type_info) == (typing.Set, (str, ), set)
    assert type_info.std_type is set

def test_tuple():
    type_info = get_type_info(typing.Tuple[str, int])
    assert generic_as_tuple(type_info) == (typing.Tuple, (str, int), tuple)
    assert type_info.std_type is tuple
