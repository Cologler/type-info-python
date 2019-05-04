# -*- coding: utf-8 -*-
#
# Copyright (c) 2019~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import typing
import collections

from type_info import get_type_info

def test_dict():
    type_info = get_type_info(typing.Dict[str, int])
    assert type_info.is_generic
    assert type_info.generic_type == typing.Dict
    assert type_info.generic_args == (str, int)
    assert type_info.dynamic_type == dict
    assert type_info.std_type is dict

def test_frozenset():
    type_info = get_type_info(typing.FrozenSet[str])
    assert type_info.is_generic
    assert type_info.generic_type == typing.FrozenSet
    assert type_info.generic_args == (str, )
    assert type_info.dynamic_type == frozenset
    assert type_info.std_type is frozenset

def test_list_opened():
    type_info = get_type_info(typing.List)
    assert type_info.is_generic
    assert type_info.generic_type == typing.List
    assert type_info.dynamic_type == list
    assert type_info.std_type is list

    assert len(type_info.generic_args) == 1
    value_type_info = type_info.generic_args[0]
    assert not value_type_info.is_generic
    assert value_type_info.is_typevar
    assert value_type_info.typevar_constraints == ()
    assert value_type_info.typevar_covariant == False
    assert value_type_info.typevar_contravariant == False

def test_list():
    type_info = get_type_info(typing.List[str])
    assert type_info.is_generic
    assert type_info.generic_type == typing.List
    assert type_info.generic_args == (str, )
    assert type_info.dynamic_type == list
    assert type_info.std_type is list

def test_set():
    type_info = get_type_info(typing.Set[str])
    assert type_info.is_generic
    assert type_info.generic_type == typing.Set
    assert type_info.generic_args == (str, )
    assert type_info.dynamic_type == set
    assert type_info.std_type is set

def test_tuple():
    type_info = get_type_info(typing.Tuple[str, int])
    assert type_info.is_generic
    assert type_info.generic_type == typing.Tuple
    assert type_info.generic_args == (str, int)
    assert type_info.dynamic_type == tuple
    assert type_info.std_type is tuple
