# -*- coding: utf-8 -*-
#
# Copyright (c) 2019~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import typing
import collections.abc

from type_info import get_type_info

def test_default_types():
    type_info = get_type_info(str)
    assert not type_info.is_generic
    assert not type_info.is_typevar
    assert not type_info.is_classvar
    assert type_info.target_type is str

def test_any():
    type_info = get_type_info(typing.Any)
    assert type_info.is_typevar
    assert type_info.typevar_constraints == ()
    assert type_info.typevar_covariant is False
    assert type_info.typevar_contravariant is False

def test_callable():
    type_info = get_type_info(typing.Callable[[str, list, dict], int])
    assert type_info.is_generic
    assert type_info.generic_type == typing.Callable
    assert type_info.generic_args == (str, list, dict, int)
    assert type_info.dynamic_type == collections.abc.Callable

def test_class_var():
    type_info = get_type_info(typing.ClassVar[typing.Dict[str, int]])
    assert type_info.is_classvar
    assert type_info.is_generic
    assert type_info.generic_type == typing.Dict
    assert type_info.generic_args == (str, int)

def test_generic():
    type_info = get_type_info(typing.Generic[typing.KT, typing.VT])
    assert type_info.is_generic
    assert type_info.generic_type == typing.Generic
    assert type_info.dynamic_type is None

def test_optional():
    type_info = get_type_info(typing.Optional[str])
    assert type_info.is_typevar
    assert type_info.typevar_constraints == (str, type(None))
    assert type_info.typevar_covariant is False
    assert type_info.typevar_contravariant is False

def test_tuple():
    pass

def test_type():
    # pep484: Type[C] refers to subclasses of C
    type_info = get_type_info(typing.Type[str])

    assert type_info.is_generic
    assert type_info.generic_type == typing.Type
    assert type_info.generic_args == (str, )
    assert type_info.std_type is type

def test_type_var():
    type_info = get_type_info(typing.TypeVar('T'))
    assert type_info.is_typevar
    assert type_info.typevar_constraints == ()
    assert type_info.typevar_covariant is False
    assert type_info.typevar_contravariant is False

    type_info = get_type_info(typing.TypeVar('T_co', covariant=True))
    assert type_info.is_typevar
    assert type_info.typevar_constraints == ()
    assert type_info.typevar_covariant is True
    assert type_info.typevar_contravariant is False

    type_info = get_type_info(typing.TypeVar('T_contra', contravariant=True))
    assert type_info.is_typevar
    assert type_info.typevar_constraints == ()
    assert type_info.typevar_covariant is False
    assert type_info.typevar_contravariant is True

def test_union():
    type_info = get_type_info(typing.Union[str, int])
    assert type_info.is_typevar
    assert type_info.typevar_constraints == (str, int)
    assert type_info.typevar_covariant is False
    assert type_info.typevar_contravariant is False

def test_any_str():
    type_info = get_type_info(typing.AnyStr)
    assert type_info.is_typevar
    assert type_info.typevar_constraints == (bytes, str)
    assert type_info.typevar_covariant is False
    assert type_info.typevar_contravariant is False

def test_text():
    type_info = get_type_info(typing.Text)
    assert not type_info.is_generic
    assert not type_info.is_typevar
    assert type_info == str
