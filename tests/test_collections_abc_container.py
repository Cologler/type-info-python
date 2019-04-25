# -*- coding: utf-8 -*-
#
# Copyright (c) 2019~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import typing
import collections.abc

from type_info import get_type_info

from utils import generic_as_tuple

def test_async_generator():
    type_info = get_type_info(typing.AsyncGenerator[str, int])
    assert generic_as_tuple(type_info) == (typing.AsyncGenerator, (str, int), collections.abc.AsyncGenerator)

def test_async_iterable():
    type_info = get_type_info(typing.AsyncIterable[str, ])
    assert generic_as_tuple(type_info) == (typing.AsyncIterable, (str, ), collections.abc.AsyncIterable)

def test_async_iterator():
    type_info = get_type_info(typing.AsyncIterator[str, ])
    assert generic_as_tuple(type_info) == (typing.AsyncIterator, (str, ), collections.abc.AsyncIterator)

def test_awaitable():
    type_info = get_type_info(typing.Awaitable[str, ])
    assert generic_as_tuple(type_info) == (typing.Awaitable, (str, ), collections.abc.Awaitable)

def test_byte_string():
    # typing.ByteString is not a generic class
    # TODO
    pass

def test_collection():
    type_info = get_type_info(typing.Collection[str, ])
    assert generic_as_tuple(type_info) == (typing.Collection, (str, ), collections.abc.Collection)

def test_container():
    type_info = get_type_info(typing.Container[str, ])
    assert generic_as_tuple(type_info) == (typing.Container, (str, ), collections.abc.Container)

def test_coroutine():
    type_info = get_type_info(typing.Coroutine[str, int, list])
    assert generic_as_tuple(type_info) == (typing.Coroutine, (str, int, list), collections.abc.Coroutine)

def test_generator():
    # pep484: The return type of generator functions can be annotated by the generic type:
    #         Generator[yield_type, send_type, return_type]
    type_info = get_type_info(typing.Generator[str, int, list])
    assert generic_as_tuple(type_info) == (typing.Generator, (str, int, list), collections.abc.Generator)

def test_hashable():
    # TODO: typing.Hashable is not a generic class
    pass

def test_items_view():
    type_info = get_type_info(typing.ItemsView[str, int])
    assert generic_as_tuple(type_info) == (typing.ItemsView, (str, int), collections.abc.ItemsView)

def test_iterable():
    type_info = get_type_info(typing.Iterable[str, ])
    assert generic_as_tuple(type_info) == (typing.Iterable, (str, ), collections.abc.Iterable)

def test_iterator():
    type_info = get_type_info(typing.Iterator[str, ])
    assert generic_as_tuple(type_info) == (typing.Iterator, (str, ), collections.abc.Iterator)

def test_keys_view():
    type_info = get_type_info(typing.KeysView[str, ])
    assert generic_as_tuple(type_info) == (typing.KeysView, (str, ), collections.abc.KeysView)

def test_mapping():
    type_info = get_type_info(typing.Mapping[str, int])
    assert generic_as_tuple(type_info) == (typing.Mapping, (str, int), collections.abc.Mapping)

def test_mapping_view():
    type_info = get_type_info(typing.MappingView[str, ])
    assert generic_as_tuple(type_info) == (typing.MappingView, (str,), collections.abc.MappingView)

def test_mutable_mapping():
    type_info = get_type_info(typing.MutableMapping[str, int])
    assert generic_as_tuple(type_info) == (typing.MutableMapping, (str, int), collections.abc.MutableMapping)

def test_mutable_sequence():
    type_info = get_type_info(typing.MutableSequence[str, ])
    assert generic_as_tuple(type_info) == (typing.MutableSequence, (str, ), collections.abc.MutableSequence)

def test_mutable_set():
    type_info = get_type_info(typing.MutableSet[str, ])
    assert generic_as_tuple(type_info) == (typing.MutableSet, (str, ), collections.abc.MutableSet)

def test_reversible():
    type_info = get_type_info(typing.Reversible[str, ])
    assert generic_as_tuple(type_info) == (typing.Reversible, (str, ), collections.abc.Reversible)

def test_sequence():
    type_info = get_type_info(typing.Sequence[str, ])
    assert generic_as_tuple(type_info) == (typing.Sequence, (str, ), collections.abc.Sequence)

def test_abstract_set():
    type_info = get_type_info(typing.AbstractSet[str, ])
    assert generic_as_tuple(type_info) == (typing.AbstractSet, (str, ), collections.abc.Set)

def test_sized():
    # TODO: typing.Sized is not a generic class
    pass

def test_values_view():
    type_info = get_type_info(typing.ValuesView[str])
    assert generic_as_tuple(type_info) == (typing.ValuesView, (str, ), collections.abc.ValuesView)
