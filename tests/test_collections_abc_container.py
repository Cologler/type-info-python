# -*- coding: utf-8 -*-
#
# Copyright (c) 2019~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import typing
import collections.abc

from type_info import get_type_info

def test_async_generator():
    type_info = get_type_info(typing.AsyncGenerator[str, int])
    assert type_info.is_generic
    assert type_info.generic_type == typing.AsyncGenerator
    assert type_info.generic_args == (str, int)
    assert type_info.dynamic_type == collections.abc.AsyncGenerator

def test_async_iterable():
    type_info = get_type_info(typing.AsyncIterable[str, ])
    assert type_info.is_generic
    assert type_info.generic_type == typing.AsyncIterable
    assert type_info.generic_args == (str, )
    assert type_info.dynamic_type == collections.abc.AsyncIterable

def test_async_iterator():
    type_info = get_type_info(typing.AsyncIterator[str, ])
    assert type_info.is_generic
    assert type_info.generic_type == typing.AsyncIterator
    assert type_info.generic_args == (str, )
    assert type_info.dynamic_type == collections.abc.AsyncIterator

def test_awaitable():
    type_info = get_type_info(typing.Awaitable[str, ])
    assert type_info.is_generic
    assert type_info.generic_type == typing.Awaitable
    assert type_info.generic_args == (str, )
    assert type_info.dynamic_type == collections.abc.Awaitable

def test_byte_string():
    # typing.ByteString is not a generic class
    # TODO
    pass

def test_collection():
    type_info = get_type_info(typing.Collection[str, ])
    assert type_info.is_generic
    assert type_info.generic_type == typing.Collection
    assert type_info.generic_args == (str, )
    assert type_info.dynamic_type == collections.abc.Collection

def test_container():
    type_info = get_type_info(typing.Container[str, ])
    assert type_info.is_generic
    assert type_info.generic_type == typing.Container
    assert type_info.generic_args == (str, )
    assert type_info.dynamic_type == collections.abc.Container

def test_coroutine():
    type_info = get_type_info(typing.Coroutine[str, int, list])
    assert type_info.is_generic
    assert type_info.generic_type == typing.Coroutine
    assert type_info.generic_args == (str, int, list)
    assert type_info.dynamic_type == collections.abc.Coroutine

def test_generator():
    # pep484: The return type of generator functions can be annotated by the generic type:
    #         Generator[yield_type, send_type, return_type]
    type_info = get_type_info(typing.Generator[str, int, list])
    assert type_info.is_generic
    assert type_info.generic_type == typing.Generator
    assert type_info.generic_args == (str, int, list)
    assert type_info.dynamic_type == collections.abc.Generator

def test_hashable():
    # TODO: typing.Hashable is not a generic class
    pass

def test_items_view():
    type_info = get_type_info(typing.ItemsView[str, int])
    assert type_info.is_generic
    assert type_info.generic_type == typing.ItemsView
    assert type_info.generic_args == (str, int)
    assert type_info.dynamic_type == collections.abc.ItemsView

def test_iterable():
    type_info = get_type_info(typing.Iterable[str, ])
    assert type_info.is_generic
    assert type_info.generic_type == typing.Iterable
    assert type_info.generic_args == (str, )
    assert type_info.dynamic_type == collections.abc.Iterable

def test_iterator():
    type_info = get_type_info(typing.Iterator[str, ])
    assert type_info.is_generic
    assert type_info.generic_type == typing.Iterator
    assert type_info.generic_args == (str, )
    assert type_info.dynamic_type == collections.abc.Iterator

def test_keys_view():
    type_info = get_type_info(typing.KeysView[str, ])
    assert type_info.is_generic
    assert type_info.generic_type == typing.KeysView
    assert type_info.generic_args == (str, )
    assert type_info.dynamic_type == collections.abc.KeysView

def test_mapping():
    type_info = get_type_info(typing.Mapping[str, int])
    assert type_info.is_generic
    assert type_info.generic_type == typing.Mapping
    assert type_info.generic_args == (str, int)
    assert type_info.dynamic_type == collections.abc.Mapping

def test_mapping_view():
    type_info = get_type_info(typing.MappingView[str, ])
    assert type_info.is_generic
    assert type_info.generic_type == typing.MappingView
    assert type_info.generic_args == (str, )
    assert type_info.dynamic_type == collections.abc.MappingView

def test_mutable_mapping():
    type_info = get_type_info(typing.MutableMapping[str, int])
    assert type_info.is_generic
    assert type_info.generic_type == typing.MutableMapping
    assert type_info.generic_args == (str, int)
    assert type_info.dynamic_type == collections.abc.MutableMapping

def test_mutable_sequence():
    type_info = get_type_info(typing.MutableSequence[str, ])
    assert type_info.is_generic
    assert type_info.generic_type == typing.MutableSequence
    assert type_info.generic_args == (str, )
    assert type_info.dynamic_type == collections.abc.MutableSequence

def test_mutable_set():
    type_info = get_type_info(typing.MutableSet[str, ])
    assert type_info.is_generic
    assert type_info.generic_type == typing.MutableSet
    assert type_info.generic_args == (str, )
    assert type_info.dynamic_type == collections.abc.MutableSet

def test_reversible():
    type_info = get_type_info(typing.Reversible[str, ])
    assert type_info.is_generic
    assert type_info.generic_type == typing.Reversible
    assert type_info.generic_args == (str, )
    assert type_info.dynamic_type == collections.abc.Reversible

def test_sequence():
    type_info = get_type_info(typing.Sequence[str, ])
    assert type_info.is_generic
    assert type_info.generic_type == typing.Sequence
    assert type_info.generic_args == (str, )
    assert type_info.dynamic_type == collections.abc.Sequence

def test_abstract_set():
    type_info = get_type_info(typing.AbstractSet[str, ])
    assert type_info.is_generic
    assert type_info.generic_type == typing.AbstractSet
    assert type_info.generic_args == (str, )
    assert type_info.dynamic_type == collections.abc.Set

def test_sized():
    # TODO: typing.Sized is not a generic class
    pass

def test_values_view():
    type_info = get_type_info(typing.ValuesView[str])
    assert type_info.is_generic
    assert type_info.generic_type == typing.ValuesView
    assert type_info.generic_args == (str, )
    assert type_info.dynamic_type == collections.abc.ValuesView
