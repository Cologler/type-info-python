# -*- coding: utf-8 -*-
#
# Copyright (c) 2019~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import typing
import collections.abc

from pytest import raises

from type_info import get_type_info

from utils import generic_as_tuple, typevar_as_tuple

def test_any():
    type_info = get_type_info(typing.Any)
    assert typevar_as_tuple(type_info) == (
        (), False, False
    )

def test_callable():
    type_info = get_type_info(typing.Callable[[str, list, dict], int])
    assert generic_as_tuple(type_info) == (
        typing.Callable, (str, list, dict, int), collections.abc.Callable
    )

def test_class_var():
    with raises(TypeError):
        get_type_info(typing.ClassVar[typing.Dict[str, int]])

    # TODO: so how can I parse class var ?

def test_generic():
    type_info = get_type_info(typing.Generic[typing.KT, typing.VT])
    assert generic_as_tuple(type_info) == (
        typing.Generic, (typing.KT, typing.VT), None
    )

def test_optional():
    type_info = get_type_info(typing.Optional[str])
    assert typevar_as_tuple(type_info) == (
        (str, type(None)), False, False
    )

def test_tuple():
    pass

def test_type():
    # pep484: Type[C] refers to subclasses of C
    type_info = get_type_info(typing.Type[str])
    typevar_as_tuple(type_info) == (
        (str), True, False
    )

def test_type_var():
    assert typevar_as_tuple(get_type_info(
        typing.TypeVar('T')
    )) == (
        (), False, False
    )
    assert typevar_as_tuple(get_type_info(
        typing.TypeVar('T_co', covariant=True)
    )) == (
        (), True, False
    )
    assert typevar_as_tuple(get_type_info(
        typing.TypeVar('T_contra', contravariant=True)
    )) == (
        (), False, True
    )

def test_union():
    type_info = get_type_info(typing.Union[str, int])
    assert typevar_as_tuple(type_info) == (
        (str, int), False, False
    )

def test_any_str():
    type_info = get_type_info(typing.AnyStr)
    assert typevar_as_tuple(type_info) == (
        (bytes, str), False, False
    )

def test_text():
    type_info = get_type_info(typing.Text)
    assert type_info == str
